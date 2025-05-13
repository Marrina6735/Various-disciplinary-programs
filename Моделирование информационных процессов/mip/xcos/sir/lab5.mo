model lab5
  Real beta = 1, nu = 0.3;
  Real s(start = .999);
  Real i(start = .001);
  Real r(start = .0);
equation
  der(s) = -beta*s*i;
  der(i) = beta*s*i - nu*i;
  der(r) = nu*i;
  annotation(
    experiment(StartTime = 0, StopTime = 30, Tolerance = 1e-06, Interval = 0.06));
end lab5;