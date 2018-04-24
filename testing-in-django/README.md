# Test Pyramid

https://martinfowler.com/bliki/TestPyramid.html

![Test Pyramid - Martin Fowler](test-pyramid.png)

# Django Test Classes

```
unittest.TestCase
├── django.test.SimpleTestCase
└── django.test.TransactionTestCase
    ├── django.test.TestCase
    └── django.test.LiveServerTestCase
```


# Usage

Default Tests

```bash
./manage.py test game.tests.tests
```

Unit Tests

```bash
./manage.py test --settings=rps.settings_unittest game.tests.tests_unit
```

Integration Tests

```bash
./manage.py test game.tests.tests_integration --keepdb
```

End To End

```bash
# chromedriver must be in $PATH
PATH=.:$PATH ./manage.py test game.tests.tests_e2e
```

Coverage

```bash
PATH=.:$PATH ./manage.py test --settings=rps.settings_coverage
```