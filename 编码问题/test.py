utf8_str = original_unicode_str.encode("utf-8")


print "is unicode=",isinstance(original_unicode_str, unicode) # True
print "uft-8 is unicode=",isinstance(utf8_str, unicode) # False
print "is str=",isinstance(original_unicode_str, str) # False
print "uft-8 is str=",isinstance(utf8_str, str) # True
print "unicode str size=", len(original_unicode_str) # 6703
print "utf8 str size =",len(utf8_str) # 7489