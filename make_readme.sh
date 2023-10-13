#!/usr/bin/env bash
#####################################################################################
# Genera la documentacion de los modulos, requiere la instalacion de gen-odoo-readme
# Lo podes instalar desde el pip asi:
#
# $ pip install gen-odoo-readme

gen-readme \
	--org-name siseservicios \
	--repo-name reves \
	--branch 16.0 \
	--addons-dir "$PWD" \
	--gen-html
