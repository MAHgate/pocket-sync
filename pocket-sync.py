import dropbox , os

client = dropbox.client.DropboxClient( 'emhVrpon3cMAAAAAAAAH9c0PBRRfWbtf5QsZyqrVcT-qU7gJz0qds-lbslCm3LV8' )
def exists( path ):
        try:
                response = client.metadata( path )
        except:
                return None
        try:
                if 'is_deleted' in response.keys():
                        if response[ 'is_deleted' ]:
                                return None
                        else:
                                return response
                else:
                        return response
        except:
                return response

pocket_txt = 'todo/Pocket/pocket.txt'
pocket_wiki = 'VimWiki/personal.wiki/pocket.wiki'
pocket_wiki_old = pocket_wiki+'~'
rev_file = '/home/ubuntu/pocket-sync/rev_file.hash'

my_meta = exists( pocket_txt )

if my_meta:

        change = True

        if 'rev' in my_meta.keys():
                new_rev = my_meta[ 'rev' ]

                if os.path.isfile( rev_file ):

                        hash_file = open( rev_file , 'r' )
                        old_rev = hash_file.readline()
                        hash_file.close()

                        if new_rev == old_rev:
                                change = False

                hash_file = open( rev_file , 'w' )
                hash_file.write( new_rev )
                hash_file.close()

        if change:

                if exists( pocket_wiki_old ):
                        response = client.file_delete( pocket_wiki_old )

                if exists( pocket_wiki ):
                        response = client.file_move( pocket_wiki , pocket_wiki_old )

                response = client.file_copy( pocket_txt , pocket_wiki )

