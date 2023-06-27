# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

MODULE := test_waves

.PHONY: check_waves
check_waves:
	$(MAKE) all
ifeq ($(SIM),questa)
	@echo "Proot"
else ifeq ($(SIM),modelsim)
	@echo "Preet"
else
	@echo "Priit"
endif

include ../../designs/sample_module/Makefile
