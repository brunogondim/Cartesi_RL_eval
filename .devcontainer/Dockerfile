FROM cartesi/dapp:Linear_Regression-devel-console
RUN apt-get update \
    && apt-get install -y python3 sqlite3 \
    && tar --sort=name --mtime="2022-01-01" --owner=1000 --group=1000 --numeric-owner -cf meutar.tar ./* 
CMD echo "rodar o comando direto no host: genext2fs -f -i 512 -b 1024 -a meutar.tar meufs.ext2" \
    && echo "rodar o comando direto no host: truncate -s %4096 meufs.ext2"