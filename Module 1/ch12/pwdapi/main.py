# -*- coding: utf-8 -*-
import falcon

from core.handlers import (
    PasswordValidatorHandler,
    PasswordGeneratorHandler,
)


validation_handler = PasswordValidatorHandler()
generator_handler = PasswordGeneratorHandler()

app = falcon.API()
app.add_route('/password/validate/', validation_handler)
app.add_route('/password/generate/', generator_handler)
