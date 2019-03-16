import sys
import es

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'request':
        f = es.Fact()
        f.request()
    elif len(sys.argv) == 2 and sys.argv[1] == 'add_fact':
        f = es.Fact()
        f.add_fact()
    elif len(sys.argv) == 2 and sys.argv[1] == 'show_all':
        f = es.Fact()
        f.show_all()
    else:
        print('Invalid arguments. Expected either "request", "add_fact" or "show_all".')
