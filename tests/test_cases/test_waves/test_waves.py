# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# GHDL unable to access signals in generate loops (gh-2594)
@cocotb.test()
async def test_waves(dut):
    cocotb.start_soon(Clock(dut.clk, 1000, "ns").start())
    dut.stream_in_data.value = 100
    dut.stream_in_data_dword.value = 200
    dut.stream_in_data_39bit.value = 300
    dut.stream_in_data_wide.value = 400
    dut.stream_in_data_dqword.value = 500
    dut.stream_in_valid.value = 1
    dut.stream_out_ready.value = 1
    dut.stream_in_real.value = 9.5
    dut.stream_in_int.value = 10
    dut.inout_if.a_in.value = 0
    dut.inout_if.b_out.value = 0
    dut.stream_in_string.value = "aa"

    await ClockCycles(dut.clk, 10)
