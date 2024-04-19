%
O0512
N10 G54; (PLANO DE TRABAJO, CERO DE LA PIEZA PUEDE SER DESDE G54 A G59)
N20 G40; (COMPENSAR DISTANCIA DE LA HERRAMIENTA AL CENTRO DE LA FRESA, G41 COMPENZA AL LADO IZQUIERDO Y G42 AL LADO DERECHO)
N30 G80; (CANCELAR CICLO DE PERFORACION)
N40 G91; (TRABAJAR CON COORDENADAS INCREMENTALES, G90 COORDENADAS ABSOLUTAS)
N50 G28 Z0; (REGRESAR A CERO EN Z)
N60 G28 X0Y0; (REGRESAR A CERO EN X Y Y)
N70 G90; (COORDENADAS ABSOLUTAS)
N80 M06 T02; (CAMBIO DE HERRAMIENTA, T02 ES EL NUMERO DE LA HERRAMIENTA)
N90 M03 S2500 F80.; (M03 CW Y M04 CCW, RPM SE DENOTA CON S Y F ES LA VELOCIDAD DE AVANCE O FEED)
N100 G00 X0Y0; (POSICIONAMIENTO DE LA HERRAMIENTA)
N110 G43 H2 Z10.; (COMPENSAR DISTANCIA DE LA HERRAMIENTA AL CENTRO DE LA FRESA, H2 ES EL NUMERO DE LA HERRAMIENTA Y Z10 ES LA DISTANCIA)
N120 G01X10.Y10.;
N130 G01Z-1.;
N140 G41 G01X10.Y30.;
N150 G01 X40.Y30.;
N160 G01 X40.Y10.;
N170 G01 Z10.;
N180 

