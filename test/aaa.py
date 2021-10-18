# Copyright 2021 Yan Yan
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

STR = """
0.0016176700592041016
0.002481698989868164
0.0027854442596435547
0.0031723976135253906
0.0017437934875488281
0.0020503997802734375
0.001399993896484375
0.0016183853149414062
0.0007357597351074219
0.0008492469787597656
0.0006558895111083984
0.0007994174957275391
0.000335693359375
0.000347137451171875
"""
"""
0.003921985626220703
0.0049707889556884766
0.0052530765533447266
0.0060312747955322266
0.0036766529083251953
0.00421142578125

0.002129793167114258
0.0023038387298583984
0.0013151168823242188
0.0015285015106201172
0.0008392333984375
0.0008127689361572266
0.0002486705780029297
0.00030994415283203125
"""

STR = """
0.0006084442138671875
0.0005354881286621094
0.0012688636779785156
0.0012619495391845703
0.002301931381225586
0.0019693374633789062
0.0038712024688720703
0.002872467041015625
0.005068302154541016
0.0047588348388671875
0.007832765579223633
0.005643367767333984
0.005807161331176758
0.004715442657470703"""
"""
0.0004992485046386719
0.0003979206085205078
0.0013720989227294922
0.0015933513641357422
0.0027768611907958984
0.0024590492248535156
0.004837512969970703
0.004601001739501953
0.009881019592285156
0.008889913558959961
0.017162084579467773
0.009079217910766602
0.009355545043945312
0.0068836212158203125
"""

nums = list(map(float, STR.strip().split("\n")))
print(sum(nums))