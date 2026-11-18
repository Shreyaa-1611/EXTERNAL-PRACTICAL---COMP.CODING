{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red185\green122\blue229;\red22\green25\blue36;\red205\green214\blue230;
\red112\green150\blue255;\red111\green213\blue190;\red167\green197\blue152;\red111\green193\blue183;}
{\*\expandedcolortbl;;\cssrgb\c78039\c57255\c91765;\cssrgb\c10980\c12941\c18824;\cssrgb\c83922\c87059\c92157;
\cssrgb\c50980\c66667\c100000;\cssrgb\c49804\c85882\c79216;\cssrgb\c70980\c80784\c65882;\cssrgb\c50196\c79608\c76863;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\cf4 \strokec4  \cf5 \strokec5 largestRectangleArea\cf4 \strokec4 (heights):\
    stack \cf6 \strokec6 =\cf4 \strokec4  []\
    ans \cf6 \strokec6 =\cf4 \strokec4  \cf7 \strokec7 0\cf4 \strokec4 \
\
    \cf2 \strokec2 for\cf4 \strokec4  i, h \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 enumerate\cf4 \strokec4 (heights \cf6 \strokec6 +\cf4 \strokec4  [\cf7 \strokec7 0\cf4 \strokec4 ]):\
        \cf2 \strokec2 while\cf4 \strokec4  stack \cf2 \strokec2 and\cf4 \strokec4  heights[stack[\cf6 \strokec6 -\cf7 \strokec7 1\cf4 \strokec4 ]] \cf6 \strokec6 >\cf4 \strokec4  h:\
            height \cf6 \strokec6 =\cf4 \strokec4  heights[stack\cf6 \strokec6 .\cf8 \strokec8 pop\cf4 \strokec4 ()]\
            width \cf6 \strokec6 =\cf4 \strokec4  i \cf2 \strokec2 if\cf4 \strokec4  \cf2 \strokec2 not\cf4 \strokec4  stack \cf2 \strokec2 else\cf4 \strokec4  i \cf6 \strokec6 -\cf4 \strokec4  stack[\cf6 \strokec6 -\cf7 \strokec7 1\cf4 \strokec4 ] \cf6 \strokec6 -\cf4 \strokec4  \cf7 \strokec7 1\cf4 \strokec4 \
            ans \cf6 \strokec6 =\cf4 \strokec4  \cf5 \strokec5 max\cf4 \strokec4 (ans, height \cf6 \strokec6 *\cf4 \strokec4  width)\
\
        stack\cf6 \strokec6 .\cf8 \strokec8 append\cf4 \strokec4 (i)\
\
    \cf2 \strokec2 return\cf4 \strokec4  ans\
\
n \cf6 \strokec6 =\cf4 \strokec4  \cf5 \strokec5 int\cf4 \strokec4 (\cf5 \strokec5 input\cf4 \strokec4 ())\
heights \cf6 \strokec6 =\cf4 \strokec4  \cf5 \strokec5 list\cf4 \strokec4 (\cf5 \strokec5 map\cf4 \strokec4 (int, \cf5 \strokec5 input\cf4 \strokec4 ()\cf6 \strokec6 .\cf8 \strokec8 split\cf4 \strokec4 ()))\
\
\pard\pardeftab720\partightenfactor0
\cf5 \strokec5 print\cf4 \strokec4 (\cf5 \strokec5 largestRectangleArea\cf4 \strokec4 (heights))\
}