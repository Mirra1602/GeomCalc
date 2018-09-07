import shape

def test_rad():
    t = shape.Triangle(3,4,60)
    assert t.rad == 1.05

def test_rad_beta():
    t = shape.Triangle(3,4,60)
    assert t.rad_beta == 0.52

def test_x():
    t = shape.Triangle(3,4,60)
    assert t.x == 2.0

def test_y():
    t = shape.Triangle(3,4,60)
    assert t.y == 3.5

def test_c():
    t = shape.Triangle(3,4,60)
    assert t.c == 3.61

def test_triangle():
    t = shape.Triangle(3,4,60)
    assert t.perimeter == 10.61 
    assert t.area == 5.2

def test_right_triangle():
    rt = shape.Right_Triangle(3,4)
    assert rt.c == 5.0
    assert rt.area == 6.0
    assert rt.perimeter == 12.0

def test_parallelogram():
    p = shape.Parallelogram(4,5, 60)
    assert p.area == 17.35
    assert p.perimeter == float(18)

def test_rectangle():
    r = shape.Rectangle(4,5)
    assert r.area == 20.0
    assert r.perimeter == 18.0

def test_square():
    s = shape.Square(3)
    assert s.area == 9.0
    assert s.perimeter == 12.0

def test_rhombus():
    rh = shape.Rhombus(3, 60)
    assert rh.area == 7.81
    assert rh.perimeter == 12.0

def test_circle():
    c = shape.Circle(3)
    assert c.area == 28.27
    assert c.circumferance == 18.85


