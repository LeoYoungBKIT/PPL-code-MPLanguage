# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u0266\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\7\34\u0100\n\34\f\34\16\34\u0103")
        buf.write("\13\34\3\34\3\34\3\35\3\35\7\35\u0109\n\35\f\35\16\35")
        buf.write("\u010c\13\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\7")
        buf.write("\36\u0116\n\36\f\36\16\36\u0119\13\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+")
        buf.write("\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\3:\3:\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\3L\3L\3M\3M\3N\3N\3O\6O\u01e6\nO\rO\16O\u01e7")
        buf.write("\3P\3P\5P\u01ec\nP\3P\6P\u01ef\nP\rP\16P\u01f0\3Q\6Q\u01f4")
        buf.write("\nQ\rQ\16Q\u01f5\3Q\3Q\7Q\u01fa\nQ\fQ\16Q\u01fd\13Q\5")
        buf.write("Q\u01ff\nQ\3Q\5Q\u0202\nQ\3Q\3Q\6Q\u0206\nQ\rQ\16Q\u0207")
        buf.write("\3Q\5Q\u020b\nQ\5Q\u020d\nQ\3R\3R\5R\u0211\nR\3S\3S\3")
        buf.write("S\3S\3S\3T\3T\3T\3T\3T\3T\3U\3U\3U\3V\3V\3V\3W\3W\3W\3")
        buf.write("X\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\3\\\3]\3]\3")
        buf.write("]\3]\3]\3]\3]\3]\5]\u023e\n]\3^\3^\3^\7^\u0243\n^\f^\16")
        buf.write("^\u0246\13^\3^\3^\3_\3_\3_\3_\5_\u024e\n_\3_\3_\3`\3`")
        buf.write("\3`\3`\3a\3a\7a\u0258\na\fa\16a\u025b\13a\3b\6b\u025e")
        buf.write("\nb\rb\16b\u025f\3b\3b\3c\3c\3c\4\u010a\u0117\2d\3\2\5")
        buf.write("\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2")
        buf.write("\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67")
        buf.write("\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20S\21U\22")
        buf.write("W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m\36o\37q")
        buf.write(" s!u\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087+\u0089")
        buf.write(",\u008b-\u008d.\u008f/\u0091\60\u0093\61\u0095\62\u0097")
        buf.write("\63\u0099\64\u009b\2\u009d\65\u009f\2\u00a1\66\u00a3\67")
        buf.write("\u00a58\u00a79\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2")
        buf.write("\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb:\u00bd;\u00bf<")
        buf.write("\u00c1=\u00c3>\u00c5?\3\2#\4\2CCcc\4\2DDdd\4\2EEee\4\2")
        buf.write("FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4")
        buf.write("\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSs")
        buf.write("s\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2")
        buf.write("ZZzz\4\2[[{{\4\2\\\\||\3\2\f\f\3\2\62;\7\2\f\f\17\17$")
        buf.write("$))^^\t\2$$))ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\17\17\"\"\2\u025a\2\67\3\2\2\2\29\3\2\2\2\2;\3\2")
        buf.write("\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3")
        buf.write("\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O")
        buf.write("\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2")
        buf.write("Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2")
        buf.write("\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2")
        buf.write("\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2")
        buf.write("\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2")
        buf.write("\2\3\u00c7\3\2\2\2\5\u00c9\3\2\2\2\7\u00cb\3\2\2\2\t\u00cd")
        buf.write("\3\2\2\2\13\u00cf\3\2\2\2\r\u00d1\3\2\2\2\17\u00d3\3\2")
        buf.write("\2\2\21\u00d5\3\2\2\2\23\u00d7\3\2\2\2\25\u00d9\3\2\2")
        buf.write("\2\27\u00db\3\2\2\2\31\u00dd\3\2\2\2\33\u00df\3\2\2\2")
        buf.write("\35\u00e1\3\2\2\2\37\u00e3\3\2\2\2!\u00e5\3\2\2\2#\u00e7")
        buf.write("\3\2\2\2%\u00e9\3\2\2\2\'\u00eb\3\2\2\2)\u00ed\3\2\2\2")
        buf.write("+\u00ef\3\2\2\2-\u00f1\3\2\2\2/\u00f3\3\2\2\2\61\u00f5")
        buf.write("\3\2\2\2\63\u00f7\3\2\2\2\65\u00f9\3\2\2\2\67\u00fb\3")
        buf.write("\2\2\29\u0106\3\2\2\2;\u0111\3\2\2\2=\u011f\3\2\2\2?\u0125")
        buf.write("\3\2\2\2A\u012e\3\2\2\2C\u0132\3\2\2\2E\u0138\3\2\2\2")
        buf.write("G\u013b\3\2\2\2I\u0142\3\2\2\2K\u0147\3\2\2\2M\u014a\3")
        buf.write("\2\2\2O\u014d\3\2\2\2Q\u0152\3\2\2\2S\u0157\3\2\2\2U\u015b")
        buf.write("\3\2\2\2W\u015e\3\2\2\2Y\u0164\3\2\2\2[\u0168\3\2\2\2")
        buf.write("]\u016f\3\2\2\2_\u0178\3\2\2\2a\u0182\3\2\2\2c\u0188\3")
        buf.write("\2\2\2e\u018d\3\2\2\2g\u0195\3\2\2\2i\u019d\3\2\2\2k\u01a4")
        buf.write("\3\2\2\2m\u01a8\3\2\2\2o\u01ac\3\2\2\2q\u01af\3\2\2\2")
        buf.write("s\u01b3\3\2\2\2u\u01b7\3\2\2\2w\u01b9\3\2\2\2y\u01bb\3")
        buf.write("\2\2\2{\u01bd\3\2\2\2}\u01bf\3\2\2\2\177\u01c1\3\2\2\2")
        buf.write("\u0081\u01c4\3\2\2\2\u0083\u01c6\3\2\2\2\u0085\u01c8\3")
        buf.write("\2\2\2\u0087\u01cb\3\2\2\2\u0089\u01ce\3\2\2\2\u008b\u01d1")
        buf.write("\3\2\2\2\u008d\u01d3\3\2\2\2\u008f\u01d5\3\2\2\2\u0091")
        buf.write("\u01d7\3\2\2\2\u0093\u01d9\3\2\2\2\u0095\u01db\3\2\2\2")
        buf.write("\u0097\u01dd\3\2\2\2\u0099\u01e0\3\2\2\2\u009b\u01e2\3")
        buf.write("\2\2\2\u009d\u01e5\3\2\2\2\u009f\u01e9\3\2\2\2\u00a1\u020c")
        buf.write("\3\2\2\2\u00a3\u0210\3\2\2\2\u00a5\u0212\3\2\2\2\u00a7")
        buf.write("\u0217\3\2\2\2\u00a9\u021d\3\2\2\2\u00ab\u0220\3\2\2\2")
        buf.write("\u00ad\u0223\3\2\2\2\u00af\u0226\3\2\2\2\u00b1\u0229\3")
        buf.write("\2\2\2\u00b3\u022c\3\2\2\2\u00b5\u022f\3\2\2\2\u00b7\u0232")
        buf.write("\3\2\2\2\u00b9\u023d\3\2\2\2\u00bb\u023f\3\2\2\2\u00bd")
        buf.write("\u0249\3\2\2\2\u00bf\u0251\3\2\2\2\u00c1\u0255\3\2\2\2")
        buf.write("\u00c3\u025d\3\2\2\2\u00c5\u0263\3\2\2\2\u00c7\u00c8\t")
        buf.write("\2\2\2\u00c8\4\3\2\2\2\u00c9\u00ca\t\3\2\2\u00ca\6\3\2")
        buf.write("\2\2\u00cb\u00cc\t\4\2\2\u00cc\b\3\2\2\2\u00cd\u00ce\t")
        buf.write("\5\2\2\u00ce\n\3\2\2\2\u00cf\u00d0\t\6\2\2\u00d0\f\3\2")
        buf.write("\2\2\u00d1\u00d2\t\7\2\2\u00d2\16\3\2\2\2\u00d3\u00d4")
        buf.write("\t\b\2\2\u00d4\20\3\2\2\2\u00d5\u00d6\t\t\2\2\u00d6\22")
        buf.write("\3\2\2\2\u00d7\u00d8\t\n\2\2\u00d8\24\3\2\2\2\u00d9\u00da")
        buf.write("\t\13\2\2\u00da\26\3\2\2\2\u00db\u00dc\t\f\2\2\u00dc\30")
        buf.write("\3\2\2\2\u00dd\u00de\t\r\2\2\u00de\32\3\2\2\2\u00df\u00e0")
        buf.write("\t\16\2\2\u00e0\34\3\2\2\2\u00e1\u00e2\t\17\2\2\u00e2")
        buf.write("\36\3\2\2\2\u00e3\u00e4\t\20\2\2\u00e4 \3\2\2\2\u00e5")
        buf.write("\u00e6\t\21\2\2\u00e6\"\3\2\2\2\u00e7\u00e8\t\22\2\2\u00e8")
        buf.write("$\3\2\2\2\u00e9\u00ea\t\23\2\2\u00ea&\3\2\2\2\u00eb\u00ec")
        buf.write("\t\24\2\2\u00ec(\3\2\2\2\u00ed\u00ee\t\25\2\2\u00ee*\3")
        buf.write("\2\2\2\u00ef\u00f0\t\26\2\2\u00f0,\3\2\2\2\u00f1\u00f2")
        buf.write("\t\27\2\2\u00f2.\3\2\2\2\u00f3\u00f4\t\30\2\2\u00f4\60")
        buf.write("\3\2\2\2\u00f5\u00f6\t\31\2\2\u00f6\62\3\2\2\2\u00f7\u00f8")
        buf.write("\t\32\2\2\u00f8\64\3\2\2\2\u00f9\u00fa\t\33\2\2\u00fa")
        buf.write("\66\3\2\2\2\u00fb\u00fc\7\61\2\2\u00fc\u00fd\7\61\2\2")
        buf.write("\u00fd\u0101\3\2\2\2\u00fe\u0100\n\34\2\2\u00ff\u00fe")
        buf.write("\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0104\u0105\b\34\2\2\u01058\3\2\2\2\u0106\u010a\7}\2")
        buf.write("\2\u0107\u0109\13\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010d\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u010e\7\177\2")
        buf.write("\2\u010e\u010f\3\2\2\2\u010f\u0110\b\35\2\2\u0110:\3\2")
        buf.write("\2\2\u0111\u0112\7*\2\2\u0112\u0113\7,\2\2\u0113\u0117")
        buf.write("\3\2\2\2\u0114\u0116\13\2\2\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\u0119\3\2\2\2\u0117\u0118\3\2\2\2\u0117\u0115\3\2\2\2")
        buf.write("\u0118\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\7")
        buf.write(",\2\2\u011b\u011c\7+\2\2\u011c\u011d\3\2\2\2\u011d\u011e")
        buf.write("\b\36\2\2\u011e<\3\2\2\2\u011f\u0120\5\5\3\2\u0120\u0121")
        buf.write("\5%\23\2\u0121\u0122\5\13\6\2\u0122\u0123\5\3\2\2\u0123")
        buf.write("\u0124\5\27\f\2\u0124>\3\2\2\2\u0125\u0126\5\7\4\2\u0126")
        buf.write("\u0127\5\37\20\2\u0127\u0128\5\35\17\2\u0128\u0129\5)")
        buf.write("\25\2\u0129\u012a\5\23\n\2\u012a\u012b\5\35\17\2\u012b")
        buf.write("\u012c\5+\26\2\u012c\u012d\5\13\6\2\u012d@\3\2\2\2\u012e")
        buf.write("\u012f\5\r\7\2\u012f\u0130\5\37\20\2\u0130\u0131\5%\23")
        buf.write("\2\u0131B\3\2\2\2\u0132\u0133\5/\30\2\u0133\u0134\5\21")
        buf.write("\t\2\u0134\u0135\5\23\n\2\u0135\u0136\5\31\r\2\u0136\u0137")
        buf.write("\5\13\6\2\u0137D\3\2\2\2\u0138\u0139\5)\25\2\u0139\u013a")
        buf.write("\5\37\20\2\u013aF\3\2\2\2\u013b\u013c\5\t\5\2\u013c\u013d")
        buf.write("\5\37\20\2\u013d\u013e\5/\30\2\u013e\u013f\5\35\17\2\u013f")
        buf.write("\u0140\5)\25\2\u0140\u0141\5\37\20\2\u0141H\3\2\2\2\u0142")
        buf.write("\u0143\5/\30\2\u0143\u0144\5\23\n\2\u0144\u0145\5)\25")
        buf.write("\2\u0145\u0146\5\21\t\2\u0146J\3\2\2\2\u0147\u0148\5\t")
        buf.write("\5\2\u0148\u0149\5\37\20\2\u0149L\3\2\2\2\u014a\u014b")
        buf.write("\5\23\n\2\u014b\u014c\5\r\7\2\u014cN\3\2\2\2\u014d\u014e")
        buf.write("\5)\25\2\u014e\u014f\5\21\t\2\u014f\u0150\5\13\6\2\u0150")
        buf.write("\u0151\5\35\17\2\u0151P\3\2\2\2\u0152\u0153\5\13\6\2\u0153")
        buf.write("\u0154\5\31\r\2\u0154\u0155\5\'\24\2\u0155\u0156\5\13")
        buf.write("\6\2\u0156R\3\2\2\2\u0157\u0158\5-\27\2\u0158\u0159\5")
        buf.write("\3\2\2\u0159\u015a\5%\23\2\u015aT\3\2\2\2\u015b\u015c")
        buf.write("\5\37\20\2\u015c\u015d\5\r\7\2\u015dV\3\2\2\2\u015e\u015f")
        buf.write("\5\5\3\2\u015f\u0160\5\13\6\2\u0160\u0161\5\17\b\2\u0161")
        buf.write("\u0162\5\23\n\2\u0162\u0163\5\35\17\2\u0163X\3\2\2\2\u0164")
        buf.write("\u0165\5\13\6\2\u0165\u0166\5\35\17\2\u0166\u0167\5\t")
        buf.write("\5\2\u0167Z\3\2\2\2\u0168\u0169\5%\23\2\u0169\u016a\5")
        buf.write("\13\6\2\u016a\u016b\5)\25\2\u016b\u016c\5+\26\2\u016c")
        buf.write("\u016d\5%\23\2\u016d\u016e\5\35\17\2\u016e\\\3\2\2\2\u016f")
        buf.write("\u0170\5\r\7\2\u0170\u0171\5+\26\2\u0171\u0172\5\35\17")
        buf.write("\2\u0172\u0173\5\7\4\2\u0173\u0174\5)\25\2\u0174\u0175")
        buf.write("\5\23\n\2\u0175\u0176\5\37\20\2\u0176\u0177\5\35\17\2")
        buf.write("\u0177^\3\2\2\2\u0178\u0179\5!\21\2\u0179\u017a\5%\23")
        buf.write("\2\u017a\u017b\5\37\20\2\u017b\u017c\5\7\4\2\u017c\u017d")
        buf.write("\5\13\6\2\u017d\u017e\5\t\5\2\u017e\u017f\5+\26\2\u017f")
        buf.write("\u0180\5%\23\2\u0180\u0181\5\13\6\2\u0181`\3\2\2\2\u0182")
        buf.write("\u0183\5\3\2\2\u0183\u0184\5%\23\2\u0184\u0185\5%\23\2")
        buf.write("\u0185\u0186\5\3\2\2\u0186\u0187\5\63\32\2\u0187b\3\2")
        buf.write("\2\2\u0188\u0189\5%\23\2\u0189\u018a\5\13\6\2\u018a\u018b")
        buf.write("\5\3\2\2\u018b\u018c\5\31\r\2\u018cd\3\2\2\2\u018d\u018e")
        buf.write("\5\5\3\2\u018e\u018f\5\37\20\2\u018f\u0190\5\37\20\2\u0190")
        buf.write("\u0191\5\31\r\2\u0191\u0192\5\13\6\2\u0192\u0193\5\3\2")
        buf.write("\2\u0193\u0194\5\35\17\2\u0194f\3\2\2\2\u0195\u0196\5")
        buf.write("\23\n\2\u0196\u0197\5\35\17\2\u0197\u0198\5)\25\2\u0198")
        buf.write("\u0199\5\13\6\2\u0199\u019a\5\17\b\2\u019a\u019b\5\13")
        buf.write("\6\2\u019b\u019c\5%\23\2\u019ch\3\2\2\2\u019d\u019e\5")
        buf.write("\'\24\2\u019e\u019f\5)\25\2\u019f\u01a0\5%\23\2\u01a0")
        buf.write("\u01a1\5\23\n\2\u01a1\u01a2\5\35\17\2\u01a2\u01a3\5\17")
        buf.write("\b\2\u01a3j\3\2\2\2\u01a4\u01a5\5\35\17\2\u01a5\u01a6")
        buf.write("\5\37\20\2\u01a6\u01a7\5)\25\2\u01a7l\3\2\2\2\u01a8\u01a9")
        buf.write("\5\3\2\2\u01a9\u01aa\5\35\17\2\u01aa\u01ab\5\t\5\2\u01ab")
        buf.write("n\3\2\2\2\u01ac\u01ad\5\37\20\2\u01ad\u01ae\5%\23\2\u01ae")
        buf.write("p\3\2\2\2\u01af\u01b0\5\t\5\2\u01b0\u01b1\5\23\n\2\u01b1")
        buf.write("\u01b2\5-\27\2\u01b2r\3\2\2\2\u01b3\u01b4\5\33\16\2\u01b4")
        buf.write("\u01b5\5\37\20\2\u01b5\u01b6\5\t\5\2\u01b6t\3\2\2\2\u01b7")
        buf.write("\u01b8\7-\2\2\u01b8v\3\2\2\2\u01b9\u01ba\7/\2\2\u01ba")
        buf.write("x\3\2\2\2\u01bb\u01bc\7,\2\2\u01bcz\3\2\2\2\u01bd\u01be")
        buf.write("\7\61\2\2\u01be|\3\2\2\2\u01bf\u01c0\7?\2\2\u01c0~\3\2")
        buf.write("\2\2\u01c1\u01c2\7>\2\2\u01c2\u01c3\7@\2\2\u01c3\u0080")
        buf.write("\3\2\2\2\u01c4\u01c5\7>\2\2\u01c5\u0082\3\2\2\2\u01c6")
        buf.write("\u01c7\7@\2\2\u01c7\u0084\3\2\2\2\u01c8\u01c9\7>\2\2\u01c9")
        buf.write("\u01ca\7?\2\2\u01ca\u0086\3\2\2\2\u01cb\u01cc\7@\2\2\u01cc")
        buf.write("\u01cd\7?\2\2\u01cd\u0088\3\2\2\2\u01ce\u01cf\7<\2\2\u01cf")
        buf.write("\u01d0\7?\2\2\u01d0\u008a\3\2\2\2\u01d1\u01d2\7]\2\2\u01d2")
        buf.write("\u008c\3\2\2\2\u01d3\u01d4\7_\2\2\u01d4\u008e\3\2\2\2")
        buf.write("\u01d5\u01d6\7<\2\2\u01d6\u0090\3\2\2\2\u01d7\u01d8\7")
        buf.write("*\2\2\u01d8\u0092\3\2\2\2\u01d9\u01da\7+\2\2\u01da\u0094")
        buf.write("\3\2\2\2\u01db\u01dc\7=\2\2\u01dc\u0096\3\2\2\2\u01dd")
        buf.write("\u01de\7\60\2\2\u01de\u01df\7\60\2\2\u01df\u0098\3\2\2")
        buf.write("\2\u01e0\u01e1\7.\2\2\u01e1\u009a\3\2\2\2\u01e2\u01e3")
        buf.write("\t\35\2\2\u01e3\u009c\3\2\2\2\u01e4\u01e6\5\u009bN\2\u01e5")
        buf.write("\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e7\u01e8\3\2\2\2\u01e8\u009e\3\2\2\2\u01e9\u01eb\t")
        buf.write("\6\2\2\u01ea\u01ec\7/\2\2\u01eb\u01ea\3\2\2\2\u01eb\u01ec")
        buf.write("\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed\u01ef\5\u009bN\2\u01ee")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3\2\2\2")
        buf.write("\u01f0\u01f1\3\2\2\2\u01f1\u00a0\3\2\2\2\u01f2\u01f4\5")
        buf.write("\u009bN\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01fe\3\2\2\2")
        buf.write("\u01f7\u01fb\7\60\2\2\u01f8\u01fa\5\u009bN\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2")
        buf.write("\u01fe\u01f7\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0201\3")
        buf.write("\2\2\2\u0200\u0202\5\u009fP\2\u0201\u0200\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u020d\3\2\2\2\u0203\u0205\7\60\2")
        buf.write("\2\u0204\u0206\5\u009bN\2\u0205\u0204\3\2\2\2\u0206\u0207")
        buf.write("\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\u020a\3\2\2\2\u0209\u020b\5\u009fP\2\u020a\u0209\3\2")
        buf.write("\2\2\u020a\u020b\3\2\2\2\u020b\u020d\3\2\2\2\u020c\u01f3")
        buf.write("\3\2\2\2\u020c\u0203\3\2\2\2\u020d\u00a2\3\2\2\2\u020e")
        buf.write("\u0211\5\u00a5S\2\u020f\u0211\5\u00a7T\2\u0210\u020e\3")
        buf.write("\2\2\2\u0210\u020f\3\2\2\2\u0211\u00a4\3\2\2\2\u0212\u0213")
        buf.write("\5)\25\2\u0213\u0214\5%\23\2\u0214\u0215\5+\26\2\u0215")
        buf.write("\u0216\5\13\6\2\u0216\u00a6\3\2\2\2\u0217\u0218\5\r\7")
        buf.write("\2\u0218\u0219\5\3\2\2\u0219\u021a\5\31\r\2\u021a\u021b")
        buf.write("\5\'\24\2\u021b\u021c\5\13\6\2\u021c\u00a8\3\2\2\2\u021d")
        buf.write("\u021e\7^\2\2\u021e\u021f\7d\2\2\u021f\u00aa\3\2\2\2\u0220")
        buf.write("\u0221\7^\2\2\u0221\u0222\7h\2\2\u0222\u00ac\3\2\2\2\u0223")
        buf.write("\u0224\7^\2\2\u0224\u0225\7t\2\2\u0225\u00ae\3\2\2\2\u0226")
        buf.write("\u0227\7^\2\2\u0227\u0228\7p\2\2\u0228\u00b0\3\2\2\2\u0229")
        buf.write("\u022a\7^\2\2\u022a\u022b\7v\2\2\u022b\u00b2\3\2\2\2\u022c")
        buf.write("\u022d\7^\2\2\u022d\u022e\7)\2\2\u022e\u00b4\3\2\2\2\u022f")
        buf.write("\u0230\7^\2\2\u0230\u0231\7$\2\2\u0231\u00b6\3\2\2\2\u0232")
        buf.write("\u0233\7^\2\2\u0233\u0234\7^\2\2\u0234\u00b8\3\2\2\2\u0235")
        buf.write("\u023e\5\u00a9U\2\u0236\u023e\5\u00abV\2\u0237\u023e\5")
        buf.write("\u00adW\2\u0238\u023e\5\u00afX\2\u0239\u023e\5\u00b1Y")
        buf.write("\2\u023a\u023e\5\u00b3Z\2\u023b\u023e\5\u00b5[\2\u023c")
        buf.write("\u023e\5\u00b7\\\2\u023d\u0235\3\2\2\2\u023d\u0236\3\2")
        buf.write("\2\2\u023d\u0237\3\2\2\2\u023d\u0238\3\2\2\2\u023d\u0239")
        buf.write("\3\2\2\2\u023d\u023a\3\2\2\2\u023d\u023b\3\2\2\2\u023d")
        buf.write("\u023c\3\2\2\2\u023e\u00ba\3\2\2\2\u023f\u0244\7$\2\2")
        buf.write("\u0240\u0243\n\36\2\2\u0241\u0243\5\u00b9]\2\u0242\u0240")
        buf.write("\3\2\2\2\u0242\u0241\3\2\2\2\u0243\u0246\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0247\3\2\2\2")
        buf.write("\u0246\u0244\3\2\2\2\u0247\u0248\b^\3\2\u0248\u00bc\3")
        buf.write("\2\2\2\u0249\u024d\5\u00bb^\2\u024a\u024b\7^\2\2\u024b")
        buf.write("\u024e\n\37\2\2\u024c\u024e\7)\2\2\u024d\u024a\3\2\2\2")
        buf.write("\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\b")
        buf.write("_\4\2\u0250\u00be\3\2\2\2\u0251\u0252\5\u00bb^\2\u0252")
        buf.write("\u0253\7$\2\2\u0253\u0254\b`\5\2\u0254\u00c0\3\2\2\2\u0255")
        buf.write("\u0259\t \2\2\u0256\u0258\t!\2\2\u0257\u0256\3\2\2\2\u0258")
        buf.write("\u025b\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2")
        buf.write("\u025a\u00c2\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025e\t")
        buf.write("\"\2\2\u025d\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u025d")
        buf.write("\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0261\3\2\2\2\u0261")
        buf.write("\u0262\bb\2\2\u0262\u00c4\3\2\2\2\u0263\u0264\13\2\2\2")
        buf.write("\u0264\u0265\bc\6\2\u0265\u00c6\3\2\2\2\27\2\u0101\u010a")
        buf.write("\u0117\u01e7\u01eb\u01f0\u01f5\u01fb\u01fe\u0201\u0207")
        buf.write("\u020a\u020c\u0210\u023d\u0242\u0244\u024d\u0259\u025f")
        buf.write("\7\b\2\2\3^\2\3_\3\3`\4\3c\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LCMT = 1
    BCMT1 = 2
    BCMT2 = 3
    BREAK = 4
    CONTINUE = 5
    FOR = 6
    WHILE = 7
    TO = 8
    DOWNTO = 9
    WITH = 10
    DO = 11
    IF = 12
    THEN = 13
    ELSE = 14
    VAR = 15
    OF = 16
    BEGIN = 17
    END = 18
    RETURN = 19
    FUNCTION = 20
    PROCEDURE = 21
    ARRAY = 22
    REAL = 23
    BOOLEAN = 24
    INTEGER = 25
    STRING = 26
    NOT = 27
    AND = 28
    OR = 29
    DIV = 30
    MOD = 31
    ADD = 32
    SUB = 33
    MUL = 34
    DIV_F = 35
    EQUAL = 36
    NOTEQUAL = 37
    LESSTHAN = 38
    GREATERTHAN = 39
    LESSEQUAL = 40
    GREATEREQUAL = 41
    ASSIGN = 42
    LSB = 43
    RSB = 44
    COLON = 45
    LB = 46
    RB = 47
    SEMI = 48
    DDOT = 49
    COMMA = 50
    INTLIT = 51
    REALIT = 52
    BOOLIT = 53
    TRUE = 54
    FALSE = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    STRLIT = 58
    IDENTIFIER = 59
    WS = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'='", "'<>'", "'<'", "'>'", "'<='", 
            "'>='", "':='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", 
            "','" ]

    symbolicNames = [ "<INVALID>",
            "LCMT", "BCMT1", "BCMT2", "BREAK", "CONTINUE", "FOR", "WHILE", 
            "TO", "DOWNTO", "WITH", "DO", "IF", "THEN", "ELSE", "VAR", "OF", 
            "BEGIN", "END", "RETURN", "FUNCTION", "PROCEDURE", "ARRAY", 
            "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", 
            "DIV", "MOD", "ADD", "SUB", "MUL", "DIV_F", "EQUAL", "NOTEQUAL", 
            "LESSTHAN", "GREATERTHAN", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", 
            "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DDOT", "COMMA", 
            "INTLIT", "REALIT", "BOOLIT", "TRUE", "FALSE", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "STRLIT", "IDENTIFIER", "WS", "ERROR_CHAR" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "LCMT", "BCMT1", "BCMT2", "BREAK", 
                  "CONTINUE", "FOR", "WHILE", "TO", "DOWNTO", "WITH", "DO", 
                  "IF", "THEN", "ELSE", "VAR", "OF", "BEGIN", "END", "RETURN", 
                  "FUNCTION", "PROCEDURE", "ARRAY", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ADD", "SUB", 
                  "MUL", "DIV_F", "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", 
                  "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "LSB", "RSB", "COLON", 
                  "LB", "RB", "SEMI", "DDOT", "COMMA", "DIGIT", "INTLIT", 
                  "EXPONENT", "REALIT", "BOOLIT", "TRUE", "FALSE", "BSP", 
                  "FF", "CR", "NEWLINE", "TAB", "SQUOTE", "DQUOTE", "BSL", 
                  "LEGAL_ESCAPE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRLIT", 
                  "IDENTIFIER", "WS", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[92] = self.UNCLOSE_STRING_action 
            actions[93] = self.ILLEGAL_ESCAPE_action 
            actions[94] = self.STRLIT_action 
            actions[97] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise IllegalEscape(self.text[1:])
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text)
     


