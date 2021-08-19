# Copyright 2021 Injective Labs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Injective Exchange API client for Python. Example only."""

import asyncio
import logging
import grpc

import injective.exchange_api.injective_derivative_exchange_rpc_pb2 as derivative_exchange_rpc_pb
import injective.exchange_api.injective_derivative_exchange_rpc_pb2_grpc as derivative_exchange_rpc_grpc

async def main() -> None:
    async with grpc.aio.insecure_channel('testnet-sentry0.injective.network:9910') as channel:
        derivative_exchange_rpc = derivative_exchange_rpc_grpc.InjectiveDerivativeExchangeRPCStub(channel)

        mkt_id = "0xd0f46edfba58827fe692aab7c8d46395d1696239fdf6aeddfa668b73ca82ea30"
        subacc = "0x4f0b9925e752f62558b8cd78c7f5a2f63c123d84000000000000000000000000"
     
        presp = await derivative_exchange_rpc.Positions(derivative_exchange_rpc_pb.PositionsRequest(market_id=mkt_id, subaccount_id=subacc))
        print("\n-- Positions Update:\n", presp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())









