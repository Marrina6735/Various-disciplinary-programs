unit Poisson_Types;

interface

const

  MAT_OK = 0; { No error }
  MAT_SINGUL = -1; { Singular matrix }
  MAT_NON_CONV = - 2;  { Non convergence of iterative procedure }
  MACHEP = 1.08420217248550444E-19; { 2^(-63) }
  ComputedEps = 1.7763568394E-15;
  StopCalculation: Boolean = false; { для остановки вычислений метода }
  Zero: double = 0.0E0;
  One: double = 1.0E0;
  OneHalf: double = 0.50E0;
  EPS = ComputedEps;

type
  TBoolVector = array of Boolean;

  TIntVector = array of Integer;
  TIntMatrix = array of TIntVector;
  TeVector = array of double;
  { добавлено е, чтобы не было совпадений с другими авторами }
  TeMatrix = array of TeVector;

  { ------------------------------------------------------------------
    Functional types
    ------------------------------------------------------------------ }

  Func1_ext = function(x: double): double;
  Func2_ext = function(x, y: double): double;
  { Function of several variables }
  TFuncNVar = function(x: TeVector): double;

  { Function of one variable }
type
  TFunc = function(x: double): double;

  { Nonlinear equation system }
type
  TEquations = procedure(x, F: TeVector);

  { Differential equation system }
type
  TDiffEqs = procedure(x: double; y, Yp: TeVector);

  { Jacobian }
type
  TJacobian = procedure(x: TeVector; D: TeMatrix);

  { Gradient }
type
  TGradient = procedure(x, G: TeVector);

  { Hessian and Gradient }
type
  THessGrad = procedure(x, G: TeVector; H: TeMatrix);

implementation

begin

end.
