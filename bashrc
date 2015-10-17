# fuck the previous executed Python script
alias fuck.py='eval $(quickfix.py --fuck $(fc -ln -1))'
# when there is a library misbehaving, you are expected to say "fuck them all"
alias fuckthemall.py='eval $(quickfix.py --fuck --all $(fc -ln -1))'
