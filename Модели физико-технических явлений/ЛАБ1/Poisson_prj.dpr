program Poisson_prj;

uses
  Forms,
  Vcl.Themes,
  Vcl.Styles,
  Poisson_Main in 'Poisson_Main.pas' {Form1},
  xycommon in '..\..\XYGraph\xycommon.pas',
  xycopy in '..\..\XYGraph\xycopy.pas' {CopyForm},
  xygraph in '..\..\XYGraph\xygraph.pas',
  xygraph3d in '..\..\XYGraph\xygraph3d.pas',
  Poisson_Types in 'Poisson_Types.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.CreateForm(TCopyForm, CopyForm);
  Application.Run;
end.
