unit Poisson_Main;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes,
  Vcl.Graphics, Vcl.Forms,
  Vcl.Dialogs,
  System.UITypes,
  Poisson_Types, Vcl.Samples.Spin, Vcl.Menus, Vcl.ComCtrls, Vcl.Controls,
  Vcl.StdCtrls, Vcl.ExtCtrls;

type
  Plot_HeaderRec = record
    SxAxis, SyAxis, SampleTitle: string;
  end;
type
  TForm1 = class(TForm)
    Panel2: TPanel;
    Panel3: TPanel;
    btReadData: TButton;
    btsavedata: TButton;
    Label1: TLabel;
    NumGrid: TSpinEdit;
    Label2: TLabel;
    ListBox1: TListBox;
    Label3: TLabel;
    ed_NpntsToDraw: TSpinEdit;
    MainMenu1: TMainMenu;
    F1: TMenuItem;
    ReadData1: TMenuItem;
    CalcDerivative1: TMenuItem;
    SaveData1: TMenuItem;
    N2: TMenuItem;
    bt_Exit: TMenuItem;
    bt_CreateCurve: TButton;
    StatusBar1: TStatusBar;
    PaintBox1: TPaintBox;
    btCopy: TButton;
    btUnZoom: TButton;
    procedure FormCreate(Sender: TObject);
    procedure btReadDataClick(Sender: TObject);
    procedure btsavedataClick(Sender: TObject);
    procedure PaintBox1Paint(Sender: TObject);
    procedure bt_ExitClick(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
    procedure btDrawApproxClick(Sender: TObject);
    procedure PaintBox1MouseDown(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure PaintBox1MouseMove(Sender: TObject; Shift: TShiftState;
      X, Y: Integer);
    procedure PaintBox1MouseUp(Sender: TObject; Button: TMouseButton;
      Shift: TShiftState; X, Y: Integer);
    procedure btUnZoomClick(Sender: TObject);
    procedure btPrintCopy(Sender: TObject);
  private
    { Private declarations }
    GridNum, NpntArtical, CurvesNum: Integer;
    // Число кривых для прорисовки графиков
    xGraph, zGraph, zzError: TeVector;
    yGraph: TeMatrix;
    xArticalGraph, yArticalGraph, zArticalGraph: TeVector;

    swAverage, swMaxErr, a, b, step: double;
    xMi, xMa, yMi, yMa: double;
    Plot_HeaderR: Plot_HeaderRec;
    Procedure DrawPlot(Plot_HeaderR: Plot_HeaderRec);
  public
    NewData: boolean;
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

uses
  math, xygraph, xycopy;

function SaveFileNameDlg(var fName: string): boolean;
var
  SaveDialog: TSaveDialog;
  OldDir: String;
begin
  // создаем диалог
  SaveDialog := TSaveDialog.Create(Application);
  SaveDialog.DefaultExt := '*.txt';
  SaveDialog.Filter := '|txt (*.txt)|*.txt';
  SaveDialog.FilterIndex := 1;
  // Where we are?
  GetDir(0, OldDir);
  // current dir
  ChDir(ExtractFileDir(fName));
  SaveDialog.InitialDir := ExtractFileDir(fName);
  // filename to write
  SaveDialog.FileName := 'Data_Out.txt';
  if SaveDialog.Execute then
  begin
    fName := SaveDialog.FileName;
    result := true;
  end
  else
    result := false;
  ChDir(OldDir);
  SaveDialog.Free;
end;

function OpenFileNameDlg(var fName: string): boolean;
var
  OpenDialog: TOpenDialog;
  OldDir: string;
begin
  OpenDialog := TOpenDialog.Create(Application);
  try
    OpenDialog.DefaultExt := '*.txt';
    OpenDialog.Filter := 'All files (*.*)|*.*|Text files (*.txt)|*.txt|';
    OpenDialog.FilterIndex := 2;
    GetDir(0, OldDir);
    ChDir(ExtractFilePath(fName));
    OpenDialog.FileName := ExtractFilePath(fName) + 'data_in.txt';
    if OpenDialog.Execute then
    begin
      fName := OpenDialog.FileName;
      result := true;
    end
    else
      result := false;
    ChDir(OldDir);
  finally
    OpenDialog.Free;
  end;
end;

procedure MinMax_XY(x: teVector; y: tematrix;
  var xMax, xMin, yMax, yMin: double);
begin
  xMax := MaxValue(x);
  xMin := MinValue(x);
  yMax := Max(MaxValue(y[1]), MaxValue(y[0]));
  yMin := Min(MinValue(y[0]), MinValue(y[1]));
end;

procedure TForm1.btReadDataClick(Sender: TObject);
var
  Ok: boolean;
  OpenedFile: TextFile;
  sw, wa, wb: double;
  DataTextName, wStr: string;
  i, OldNpoints: Integer;
begin
  DataTextName := Application.ExeName; // для определения текущего каталога
  if OpenFileNameDlg(DataTextName) then // если задано имя файла для чтения, то
  begin
{$I-}
    // открываем файл для чтения
    AssignFile(OpenedFile, DataTextName);
    Reset(OpenedFile);
{$I+}
    Ok := (IoResult = 0); // открылся?
    try
      if Ok then // открылся
      begin
        OldNpoints := NpntArtical;
        NpntArtical := 0;
        // цикл по определению количества строк в файле
        // в строке есть по крайней мере три числа
        while not Eof(OpenedFile) do
        begin
          Readln(OpenedFile, wStr);
//          if Get1Extended_AnyDivider(wStr, wa, false) then
//            if Get1Extended_AnyDivider(wStr, wb, false) then
//              inc(NpntArtical);
        end;
        // конец цикла по определению количества строк в файле
        if NpntArtical > 0 then
        begin
          NpntArtical := NpntArtical - 1;
          Reset(OpenedFile);
          /// /          SetLength(xArg, succ(NpntArtical)); // аргумент
          // SetLength(zVector, succ(NpntArtical)); // функция (и в y[0,i])
          // SetLength(yMatr, 2, succ(NpntArtical));
          for i := 0 to NpntArtical do
          begin
            Readln(OpenedFile, wStr);
            // Get1Extended_AnyDivider(wStr, xArg[i], false);
            // Get1Extended_AnyDivider(wStr, yMatr[0, i], false);
            // Get1Extended_AnyDivider(wStr, yMatr[1, i], false);
            // zVector[i] := yMatr[0, i];
            // y[1, i] := 0;
            // Обнуляем для прорисовки, если не отработает дифференцирование
          end;
          // MinMax_XYlxArg, yMatr, xMax, xMin, yMax, yMin);
          NewData := true;
        end
        else // файл пуст - ничего не надо считать
        begin
          NpntArtical := OldNpoints;
          NewData := false;
        end;
      end
      else
      begin
        MessageDlg('Could not open file', mtInformation, [mbOk], 0);
      end;
      // Заполнение параметров расчета
      sw := 1000;
      // for i := 0 to NpntArtical do
      // begin
      // if zVector[i] < sw then
      // begin
      // // Точка минимума
      // // RForSimplex.nMin := i;
      // // Номер точки с минимальным значением массива Z
      // sw := zVector[i];
      // end;
      // end;
      sw := 0;
      OldNpoints := 0;
    finally
      if Ok then
        CloseFile(OpenedFile);
    end;
  end;
  StatusBar1.Panels[0].Text := 'File: ' + DataTextName;
  with Plot_HeaderR do
  begin
    SxAxis := 'x';
    SyAxis := 'y';
    SampleTitle := '';
  end;
  DrawPlot(Plot_HeaderR);
end;

Procedure TForm1.DrawPlot(Plot_HeaderR: Plot_HeaderRec);
var
  scale: single;
  x1, y1, x2, y2, dx1, dy1, dx2, dy2: Integer;
  noclip: boolean;
  // mi, xma, ymi, yma,
  zzmi, zzma: double;
  incr, zmx: single;
  txtx, txty: string;
  typegr: Integer;
  grid, log, fix: boolean;
  i, jCurve: Integer;
begin
  // Form1.PaintBox1.Refresh;
  scale := 1;
  x1 := 10; // (%)
  x2 := 100 - x1;
  y1 := 15;
  y2 := 100 - y1;
  dx1 := 0;
  dx2 := 0;
  dy1 := 0;
  dy2 := 0;
  noclip := true;
  xMa := MaxValue(xGraph);
  xMi := MinValue(xGraph);
  yMa := MaxValue(yGraph[0]);
  yMi := MinValue(yGraph[0]);
  for i := 1 to CurvesNum - 1 do
  begin
    yMa := Max(yMa, MaxValue(yGraph[i]));
    yMi := Min(yMi, MinValue(yGraph[i]));
  end;
  if zGraph <> nil then
  begin
    yMa := Max(yMa, MaxValue(zGraph));
    yMi := Min(yMi, MinValue(zGraph));
  end;

  incr := 0;
  zmx := 0;
  txtx := 'Ось xGraph';
  txty := 'Ось yGraph';
  with Plot_HeaderR do
  begin
    if SxAxis <> '' then
      txtx := SxAxis;
    if SyAxis <> '' then
      txty := '@' + SyAxis;
  end;
  grid := false;
  log := false;
  fix := false;
  typegr := 1;
  xycleargraph(Form1.PaintBox1, clWhite, clBlack, 1.1);
  xystartgraph(10, 90, 15, 85, 0, 0, 0, 0, clipon);
  // xycleargraph(PaintBox1, clGradientInactiveCaption { clWhite } ,
  // clBlack, scale);
  // xystartgraph(x1, x2, y1, y2, dx1, dx2, dy1, dy2, noclip);

  // xyxaxis(clBlack, xmi, xma, incr, zmx, txtx, grid, log, fix);
  // xyyaxis(clBlack, ymi, yma, incr, zmx, txty, typegr, grid, log, fix);

  xyxaxis(clBlack, xMi, xMa, 0, 0, txtx, 1, false, false, fixed, 0);
  xyyaxis(clBlack, yMi, yMa, 0, 0, txty, 1, false, false, fixed);

  xypen.Width := 2;
  for jCurve := 0 to CurvesNum - 1 do
  begin
    case jCurve of
      0:
        xypen.Color := clGreen;
      1:
        xypen.Color := clBlue;
      2:
        xypen.Color := clRed;
    else
      xypen.Color := clBlack;
    end;
    xymove(xGraph[0], yGraph[jCurve, 0]);
    for i := 1 to NpntArtical do
      xydraw(xGraph[i], yGraph[jCurve, i]);
  end;
  if zGraph <> nil then
  begin
    xypen.Color := clFuchsia;
    xypen.Width := 1;
    xymove(xGraph[0], zGraph[0]);
    for i := 1 to NpntArtical do
      xydraw(xGraph[i], zGraph[i]);
  end;

  if zzError <> nil then
  begin
    zzma := MaxValue(zzError);
    zzmi := MinValue(zzError);
    // log := true;
    if zzError <> nil then
    begin
      zzma := Max(zzma, MaxValue(zzError));
      zzmi := Min(zzmi, MinValue(zzError));
    end;

    // zzma := Max(zzma, MaxValue(zzError));
    // zzmi := Min(zzmi, MinValue(zzError));
    // xyyaxis(clRed, zzmi, zzma, 0, 0, '@residual', 4, false, true, sci);
    xyyaxis(clRed, zzmi, zzma, 0, 0, '@residual', 4, false, log, sci);
    xypen.Color := clRed;
    xypen.Width := 1;
    xymove(xGraph[0], zzError[0]);
    for i := 1 to NpntArtical do
      xydraw(xGraph[i], zzError[i]);
    if zzError <> nil then
    begin
      xypen.Color := clFuchsia;
      xymove(xGraph[0], zzError[0]);
      for i := 1 to NpntArtical do
        xydraw(xGraph[i], zzError[i]);
    end;
  end;

  xydeffont;

  { - - - additional instructions - - - }
  (*
    // Legend
    // HOW TO MAKE A LEGEND: XYARRAYLEGENDS
    xysetfont('Times New Roman', 10, 1, 2, 0);
    // xytext(clBlack, ' Eps = 0.1 ', xMa - 0.05, yMa + 0.05, 1, -1, 2);
    xylinewidth(1);
    for jCurve := 0 to CurvesNum - 1 do
    begin
    case jCurve of
    0:
    begin
    xypen.Color := clGreen;
    XYLegendEntry(0, 'Eps = ' + floatToStrF(eps_ParamCurrent[0],
    ffExponent, 2, 2));
    end;
    1:
    begin
    xypen.Color := clRed;
    XYLegendEntry(0, 'Eps = ' + floatToStrF(eps_ParamCurrent[1],
    ffExponent, 2, 2));
    end;
    2:
    begin
    xypen.Color := clBlue;
    XYLegendEntry(0, 'Eps = ' + floatToStrF(eps_ParamCurrent[2],
    ffExponent, 2, 2));
    end;
    else
    begin
    xypen.Color := clBlack;
    XYLegendEntry(0, 'Eps = ' + floatToStrF(eps_ParamCurrent[3],
    ffExponent, 2, 2));
    end;
    end;
    end;
    // xysetlinestyle(5, 0,0);//:integer;lspacing:integer[lslope:single);
    // xylinewidth(1);
    // xypen.style := psDashDot;
    // xysetlinestyle(-1, 0,0);//:integer;lspacing:integer[lslope:single);
    // XYLegendEntry(0,'Re(τe)');
    xylegendmake(0, PaintBox1.Width div 2, 10, 0, 1, 0,
    // round(PaintBox1.height * 0.55)
    0, 0, frameoff);
    // XYLegendMake(0, 600, 400, 0, 0, 50, 50, 10, false);
  *)
  xydeffont;

  if Plot_HeaderR.SampleTitle <> '' then
  begin
    // SampleTitle := 'Blue=x, Red = y, Black = z';
    xysetusercoordinates(0, 0);
    xytitle(clBlack, '@' + Plot_HeaderR.SampleTitle);
  end;
  xyinitruler(clgray, 30, 20, 1, 0 + 16);

  // xyinitruler(clgray, 20, round(PaintBox1.height * 0.65) - xycharheight div 2,
  // 1, 0 + 8);
  xyfinish;

end;

procedure TForm1.FormClose(Sender: TObject; var Action: TCloseAction);
begin
  xGraph := nil;
  yGraph := nil;
  zGraph := nil;
  zzError := nil;
  // zzErrorRKF := nil;
  xArticalGraph := nil;
  yArticalGraph := nil;
  zArticalGraph := nil;
end;

procedure TForm1.FormCreate(Sender: TObject);
var
  i: Integer;
begin
  // Начальные установки
  FormatSettings.DecimalSeparator := '.'; { SetSysConst; }
  FormatSettings.DateSeparator := '.';
  // График - заставка
  a := -2;
  b := 3.5;
  NpntArtical := 260;
  CurvesNum := 2;
  step := (b - a) / NpntArtical; // step
  SetLength(xGraph, succ(NpntArtical));
  SetLength(yGraph, CurvesNum, succ(NpntArtical));
  for i := 0 to NpntArtical do
  begin
    xGraph[i] := a + i * step;
    yGraph[0, i] := sqr(xGraph[i]) * cos(4 * xGraph[i]);
    yGraph[1, i] := sqr(xGraph[i]) * sin(4 * xGraph[i]);
  end;
  MinMax_XY(xGraph, yGraph, xMa, xMi, yMa, yMi);
  NewData := false;
  ListBox1.ItemIndex :=0;
end;

procedure TForm1.btsavedataClick(Sender: TObject);
var
  Ok: boolean;
  i: Integer;
  SaveFile: TextFile;
  DataTextName: string;

begin
  DataTextName := Application.ExeName; // to determine the current directory
  if SaveFileNameDlg(DataTextName) then
  // if a file name is selected for recording, then
  begin
{$I-}
    // открываем файл для записи
    AssignFile(SaveFile, DataTextName);
    Rewrite(SaveFile);
{$I+}
    Ok := (IoResult = 0); // открылся?
    try
      if Ok then // открылся
      begin
        // WriteLN(SaveFile, 'График функции ');
        // WriteLN(SaveFile, 'Число точек ', #9, NpntArtical:2, #9);
        for i := 0 to NpntArtical do
        begin
          WriteLN(SaveFile, xGraph[i]:14:9, #9, yGraph[0, i]:14:9, #9,
            yGraph[1, i]:14:9);
        end;
      end
      else
      begin
        MessageDlg('Файл не открылся', mtInformation, [mbOk], 0);
      end;
    finally
      if Ok then
        CloseFile(SaveFile);
    end;
  end;
end;

procedure TForm1.bt_ExitClick(Sender: TObject);
begin
  Close();
end;

procedure TForm1.btUnZoomClick(Sender: TObject);
begin
  { ­ change the settings of the graph here }

  xyunzoom; // master zoom reset

  PaintBox1.repaint; // actually plot the new graph

end;

procedure TForm1.btPrintCopy(Sender: TObject);
begin
  xycopystart;
end;

procedure showdata;
begin
end;

procedure TForm1.PaintBox1MouseDown(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
  xyexportd.xp := -1;
  xymousedown(Button, Shift, X, Y);
end;

procedure TForm1.PaintBox1MouseMove(Sender: TObject; Shift: TShiftState;
  X, Y: Integer);
begin
  XYMouseMove(Shift, X, Y);
  if (xyexportd.xp >= 0) and (xyexportd.igr = 1) and not(ssCtrl in Shift) then
    showdata;
end;

procedure TForm1.PaintBox1MouseUp(Sender: TObject; Button: TMouseButton;
  Shift: TShiftState; X, Y: Integer);
begin
  xyexportd.xp := -1;
  // Edit1.hide;
  XYMouseUp(Button, Shift, X, Y);
end;

procedure TForm1.PaintBox1Paint(Sender: TObject);
begin
  DrawPlot(Plot_HeaderR);
end;

// задача: Example 10.1 Mason for y''(x) = f(x) = (3*x^2+14 * x+9) * exp(x) // (2x+1) exp(x)
function DerivTwoPoisson_01(x: double): double;
begin
  result := (power(x,2) + 4*x + 4) * exp(x);//(3*power(x,2)+14 * x+9) * exp(x);//(2 * x + 5) * exp(x);
end;

function DerivPoisson_01(x: double): double;
begin
  result := (power(x,2) + 3*x + 2) * exp(x);//(3*power(x,2)+ 6* x+2) * exp(x);//(2 * x + 3) * exp(x);
end;

function Exact_Poisson_01(x: double): double;
begin
  result := (power(x,2) + 2*x - 1) * exp(x);//(3*power(x,2) + 2*x - 1)*exp(x);//(2 * x + 1) * exp(x);
end;

// Example 10.1 Mason (10.18) u'' + 6 abs(x)=0, u(+-1)=0
function DerivTwoPoisson_02(x: double): double;
begin
  result := -6 * abs(x);
end;

function DerivPoisson_02(x: double): double;
begin
  if x > 0 then
    result := -3 * sqr(x)
  else
    result := 3 * sqr(x);
end;

// Example 10.1 Mason (10.18) u'' + 6 abs(x)=0, u(+-1)=0
// exact solution: 1-sqr(x)*abs(x);
function Exact_Poisson_02(x: double): double;
begin
  result := 1 - sqr(x) * abs(x);
end;

procedure M_AtxV_B(n: Integer; const A: TeMatrix; const B: TeVector;
  var R: TeVector);
var // произведение транспонированной матрицы A на вектор B : R := A'*B
  Rm: double;
  i, K: Integer;
begin
  for i := 0 to n do
  begin
    Rm := 0.0;
    for K := 0 to n do
      Rm := Rm + A[K, i] * B[K];
    R[i] := Rm;
  end;
end;


procedure M_AxV_B(n: Integer; const A: TeMatrix; const B: TeVector;
  var R: TeVector);
var // произведение матрицы A на вектор B : R := A'*B
  Rm: double;
  i, K: Integer;
begin
  for i := 0 to n do
  begin
    Rm := 0.0;
    for K := 0 to n do
      Rm := Rm + A[i, K] * B[K];
    R[i] := Rm;
  end;
end;

procedure MxM(n: Integer; A, B: TeMatrix; var R: TeMatrix);
var // произведение матриц R := A*B
  Rm: double;
  i, J, K: Integer;
begin
  for i := 0 to n do
    for J := 0 to n do
    begin
      Rm := 0;
      for K := 0 to n do
      begin
        Rm := Rm + A[i, K] * B[K, J];
      end;
      R[i, J] := Rm;
    end;
end;

Procedure NodesChebLobatto(Const n: integer; var ET: TeVector;
  natural_order: boolean);

// **********************************************************************
// *   COMPUTES THE NODES RELATIVE TO THE CHEBYSHEV GAUSS-LOBATTO FORMULA
// *   N  = ORDER OF THE FORMULA
// *   ET = VECTOR OF THE NODES, ET(I), I=0,N
// **********************************************************************
var
  i, n2: integer;
  c, etx: double;
begin
  IF (n > 0) then
  begin
    if natural_order then
    begin
      ET[0] := -1.0;
      ET[n] := 1.0;
    end
    else
    begin
      ET[0] := 1.0;
      ET[n] := -1.0;
    end;
    IF (n > 1) then
    begin
      n2 := (n - 1) div 2; // (N-1)/2;
      ET[n2 + 1] := 0.0;
      IF (n > 2) then
      begin
        // PI = 3.14159265358979323846D0
        c := PI / n;
        for i := 1 to n2 do
        begin
          etx := COS(c * i);
          if natural_order then
          begin
            ET[i] := -etx;
            ET[n - i] := etx;
          end
          else
          begin
            ET[i] := etx;
            ET[n - i] := -etx;
          end;
        end;
      end;
    end;
  end;
END;

Procedure ValueOfChebPolinomial(Const n: integer; Const X: double;
  Var Y, DY, D2Y: double);
// ***************************************************************
// *   COMPUTES THE VALUE OF THE CHEBYSHEV POLYNOMIAL OF DEGREE N
// *   AND ITS FIRST AND SECOND DERIVATIVES AT A GIVEN POINT
// *   N  = DEGREE OF THE POLYNOMIAL
// *   X  = POINT IN WHICH THE COMPUTATION IS PERFORMED
// *   Y  = VALUE OF THE POLYNOMIAL IN X
// *   DY = VALUE OF THE FIRST DERIVATIVE IN X
// *   D2Y= VALUE OF THE SECOND DERIVATIVE IN X
// ***************************************************************
var
  k: integer;
  Ym, Dym, D2ym, Yp, Dyp, D2yp: double;
begin
  Y := 1.0;
  DY := 0.0;
  D2Y := 0.0;
  IF (n > 0) then
  begin
    Y := X;
    DY := 1.0;
    D2Y := 0.0;
    IF (n > 1) then
    begin
      Yp := 1.0;
      Dyp := 0.0;
      D2yp := 0.0;
      for k := 2 to n do
      begin
        Ym := Y;
        Y := 2.0 * X * Y - Yp;
        Yp := Ym;
        Dym := DY;
        DY := 2.0 * X * DY + 2.0 * Yp - Dyp;
        Dyp := Dym;
        D2ym := D2Y;
        D2Y := 2.0 * X * D2Y + 4.0 * Dyp - D2yp;
        D2yp := D2ym;
      end;
    end;
  end;
END;

procedure InverseToDeriveAmiraslani(n: integer; DInverse: teMatrix);
// Fill in the matrix inverse to the differentiation matrix
// in the spectral representation of Amiraslani ,
var
  i, j: integer;
begin

  // Заполнение матрицы, обратной к матрице дифференцирования
  // в спектральном представлении Amiraslani ,
  //
  for i := 0 to n do
  begin
    for j := 0 to n do
      DInverse[i, j] := 0; // // Обнуление
    if i = 1 then
    begin
      DInverse[i, i-1] := 1;
      DInverse[i, i + 1] := -1 / 2;
//      DInverse[i, i + 1] := -2;//-1 / 2;
    end;
    if (i > 1) and (i <= n - 1) then
    begin
      DInverse[i, i-1] := 1 / (2 * i);
//      DInverse[i, i-1] := 2*i;//1 / (2 * i);
      DInverse[i, i + 1] := -DInverse[i, i-1];
    end;
    if (i = n ) then
    begin
      DInverse[i, i-1] := 1 / (2 * i);
//      DInverse[i, i-1] := 2*i;//1 / (2 * i);
    end;
  end;
end;

Procedure PoissonEquation_Fornberg(a, b: double; n: Integer;
  leftBound, RightBound: double; DerivTwoFunc: Func1_ext;
  NpntArtical: Integer;
  var Argvalues, Funcvalues: teVector);
var
  i, j: Integer;
  hm, hp, dy, d2y, wodd, weven, wt: double;
  xRealW, xCheb, fr,
//  Testfr, Workfr,
  solution: teVector;
  t: TeMatrix;
  DInverse: TeMatrix;
  D2: TeMatrix;


  // Уравнение Пуассона (Аппроксимация производной).docx
  // Условия Дирихле
  // Уравнение Пуассона- восстановление функции по заданной второй производной и по
  // двум дополнительном условиям на левом и на правом конце
  //
  // Интервал интегрирования [a, b]
  // n - число точек сетки - размерность базиса
  // leftBound - Условие на левом конце - начальное для диф уравнения
  // RightBound - Условие на правом конце - граничное для диф уравнения
  // TakeLeftBound : true - использовать заданное граничное условие на левом конце интервала
  // GridFromLeft -  true {сетка генерируется в natural_order: [-1,1], false - [+1, -1]}
  // DerivFunc: Func1_ext; Функция, вычисляющая правую часть - вторая производная решения
  //
  // NpntArtical : integer; - размерность входного массивв Argvalues и выходного Funcvalues
  // var Argvalues, - массив значений аргументов, для которых надо рассчитать решение

  // Funcvalues: TeVector - вычисленное решение

  // Алгоритм:        y''(x) = f(x), y(a)=ya. y(b)=yb

  // Вычисляем коэффициенты разложения функции f(x) - задающей значения производной
  // по формуле 2.1.3. (Fornberg)
  // определяем коэффициенты искомой функции  (кроме a0, a1)
  // вычисляем a0,a1 из граничных условий

begin
  hm := (b - a) * 0.5;
  hp := (b + a) * 0.5;
  setLength(xCheb, succ(n)); // сетка Чебышева внутри процедуры расчета
  setLength(xRealW, succ(n)); // соответствующая сетка интервала [a,b]
  setLength(fr, succ(n)); //
//  setLength(Testfr, succ(n)); //
//  setLength(Workfr, succ(n)); //
  setLength(solution, succ(n));
//   setLength(DifM, succ(n - 1), succ(n - 1));
  setLength(DInverse, succ(n), succ(n));
  // setLength(dWork, succ(n), succ(n));
  setLength(t, succ(n), succ(n)); // матрица полиномов Чебышева

  setLength(D2, succ(n), succ(n));
  // Внутренний расчет ведется на сетке Гаусса-Лобатто,
  // снаружи задается вектор абсцисс Argvalues,
  // для которого надо определить вектор решений
  // Результат выдается в массивах  Argvalues (входной), Funcvalues (выходной)
  // размерности которых задаются извне

  NodesChebLobatto(n, xCheb, true); // true { natural_order: [-1,1]}
  // false - Integration grid from +1 to -1
  for i := 0 to n do
  begin
    if (i = 0) then
      xRealW[0] := a
    else if (i = n) then
      xRealW[n] := b
    else
      xRealW[i] := hm * xCheb[i] + hp;

    // right-hand side vector in real space
    fr[i] := DerivTwoFunc(xRealW[i]) * sqr(hm);
    //  to take into account discrete orthogonality
    if (i = 0) or (i = n) then
      fr[i] := fr[i] / sqrt(2);
    solution[i] := fr[i]; // solution[i] := fr[i]; working array
    // Chebyshev coefficients on [-1,1]
    for j := 0 to n do
    begin
      // T - filling the matrix with the values of Chebyshev polynomials
      ValueOfChebPolinomial(j, xCheb[i], t[i, j], dy, d2y);
    //  to take into account discrete orthogonality
      if (i = 0) or (i = n) then
        t[i, j] := t[i, j] / sqrt(2);
    end;

  end;

  M_AtxV_B(n, t, solution, fr); // New vector of Linear system

  for i := 1 to n - 1 do // Calculation of coefficients
    fr[i] := fr[i] / (n / 2);
  fr[0] := fr[0] / n;
  fr[n] := fr[n] / n;
  // Calculation of integration matrix
  InverseToDeriveAmiraslani(n, DInverse);
  // Squared matrix of integration in D2
  MxM(n, DInverse, DInverse, D2);
  // Coeffitients of the function we wanted to find
  M_AxV_B(n, D2, fr, solution);

  solution[0] := 0;
  solution[1] := 0;

  wodd := 0;
  weven := 0;
  for i := 2 to n do
  begin
    if odd(i) then
      wodd := wodd + solution[i]
    else
      weven := weven + solution[i];
  end;

  solution[0] := 0.5 * (-2 * weven + leftBound + RightBound);
  solution[1] := 0.5 * (-2 * wodd - leftBound + RightBound);

  // Пересчет значений найденной функции на требуемую сетку
  // Argvalues (input array), Funcvalues - result  wodd, weven, wt
  for i := 0 to NpntArtical do
  begin
    // Argvalues[i] := x[i];
    wt := (2 * Argvalues[i] - b - a) / (b - a);
    wodd := 0;
    for j := 0 to n do
    begin
      ValueOfChebPolinomial(j, wt, weven, dy, d2y);
      wodd := wodd + weven * solution[j];
    end;
    Funcvalues[i] := wodd;
  end;

  xCheb := Nil;
  xRealW := nil;
  fr := nil;
  solution := nil;
  t := nil;
  // dWork := nil;
//   DifM := nil;
  DInverse := nil;
  D2 := nil;
//  Workfr := nil;
//  Testfr := nil;
end;

procedure UniformMesh(a, b: double; GridNum: Integer; xGraph: TeVector);
// Uniform grid for drawing charts
var
  Step: double;
  i: Integer;
begin
  Step := (b - a) / GridNum;
  xGraph[0] := a;
  xGraph[GridNum] := b;
  for i := 1 to GridNum-1 do
      xGraph[i] := a + i * Step;

end;


procedure TForm1.btDrawApproxClick(Sender: TObject);
var
  problem: Integer;
  FuncAtLeft, FuncAtRight: double;

  procedure fillForGraph(exactSolution: TFunc);
  var
    i: Integer;
  begin
    swAverage := 0;
    swMaxErr := 0;
    for i := 0 to NpntArtical do
    begin

      yGraph[0, i] := zzError[i]; // green - решение на равномерной сетке
      // средневзвешенная ошибка
      swAverage := swAverage + ABS(exactSolution(xGraph[i]) - zzError[i]);

      yGraph[1, i] := exactSolution(xGraph[i]);
      // blue - точное решение на равномерной сетке

      zzError[i] := ABS(exactSolution(xGraph[i]) - yGraph[0, i]); // red невязка

    end;
    swMaxErr := Max(ABS(MaxValue(zzError)), ABS(MinValue(zzError)));
    swAverage := swAverage / NpntArtical;
  end;

begin


  problem := ListBox1.ItemIndex+1;
//  interval boundaries
    case problem of
      1:
        begin
          a := -3; // left boundary
          b := 1; // right boundary
        end;
      2:
        begin
          a := -1;
          b := 1;
        end;
    end;

    GridNum := round(NumGrid.Value);   // Collocation points
    NpntArtical := ed_NpntsToDraw.Value;   // number of drawing points
    step := (b - a) / NpntArtical; // step
    CurvesNum := 2; // graphs number
    SetLength(yGraph, succ(CurvesNum), succ(NpntArtical));
    SetLength(xGraph, succ(NpntArtical));
    SetLength(zzError, succ(NpntArtical));
    UniformMesh(a, b, NpntArtical, xGraph);
    case problem of
      1:
        begin
          // equation like in Example 10.1 Mason for y''(x) = f(x)
          // exact solution: y =(2x+1) exp(x)
          FuncAtLeft :=  Exact_Poisson_01(a);
          FuncAtRight := Exact_Poisson_01(b);
          PoissonEquation_Fornberg(a, b, GridNum, FuncAtLeft, FuncAtRight,
            DerivTwoPoisson_01, NpntArtical, xGraph, zzError);
          fillForGraph(Exact_Poisson_01);
          Plot_HeaderR.SampleTitle := 'equation y'''' = (2 * x + 1) * exp(x)';

        end;
      2:
        begin
          // equation : Example 10.1 Mason (10.18) u'' + 6 abs(x)=0, u(+-1)=0
          // exact solution: 1-sqr(x)*abs(x);
          FuncAtLeft := Exact_Poisson_02(a); // Значение функции на левом конце
          FuncAtRight := Exact_Poisson_02(b);
          // Значение функции на правом конце
          PoissonEquation_Fornberg(a, b, GridNum, FuncAtLeft, FuncAtRight,
            DerivTwoPoisson_02, NpntArtical, xGraph, zzError);
          fillForGraph(Exact_Poisson_02);
          Plot_HeaderR.SampleTitle := 'equation y'''' + 6 abs(x)=0, y(+-1)=0';

        end;
    end;


    // Example 10.1 Mason
    // Эффектнее будет выглядеть на интервале [-1,0]
    // с нулевой производной на правом конце
    // sw := sw + ABS(Exact_Poisson_02(xGraph[i]) -
    // zzError[i]);
    // zzError[i] := (Exact_Poisson_02(xGraph[i]) -
    // yGraph[0, i]); // red невязка
    // yGraph[1, i] := Exact_Poisson_02(xGraph[i]); // blue - exact solutioon
    // sw := 0;
    // swMax := 0;

  with Plot_HeaderR do
  begin
    SxAxis := 'x';
    SyAxis := 'y';
    // SampleTitle := 'Initial Graph';
  end;
  DrawPlot(Plot_HeaderR);
end;

end.
