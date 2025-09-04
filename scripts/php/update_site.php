<?php

### Vars definitions
$WEB_DIR = "/var/www/";
$SITE_DIRNAME = "10s25";
$LATEST_RELEASE_SRC = "https://github.com/10s25/site/archive/refs/tags/last.tar.gz";
$LATEST_RELEASE_DIRNAME = "site-last";
$LATEST_RELEASE_FILE = "last.tar.gz";

### Fonction definition
function removeDir(string $dir): void {
    if(is_dir($dir)){
        $it = new RecursiveDirectoryIterator($dir, RecursiveDirectoryIterator::SKIP_DOTS);
        $files = new RecursiveIteratorIterator($it,
                     RecursiveIteratorIterator::CHILD_FIRST);
        foreach($files as $file) {
            if ($file->isDir()){
                rmdir($file->getPathname());
            } else {
                unlink($file->getPathname());
            }
        }
        rmdir($dir);
    }
}

### Update
chdir($WEB_DIR);
unlink($LATEST_RELEASE_FILE);
unlink('last.tar');
removeDir("$WEB_DIR/$LATEST_RELEASE_DIRNAME");

$tarFile = fopen($LATEST_RELEASE_FILE, "w");
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $LATEST_RELEASE_SRC);
curl_setopt($ch, CURLOPT_FAILONERROR, true);
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_AUTOREFERER, true);
curl_setopt($ch, CURLOPT_BINARYTRANSFER,true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_FILE, $tarFile);
$page = curl_exec($ch);
if(!$page) {
echo "Error :- ".curl_error($ch);
}
curl_close($ch);

# decompress from gz
$p = new PharData($LATEST_RELEASE_FILE);
$p->decompress();
# unarchive from the tar
$phar = new PharData($LATEST_RELEASE_FILE);
$phar->extractTo($WEB_DIR);

removeDir("$WEB_DIR/$SITE_DIRNAME");
rename("$WEB_DIR/$LATEST_RELEASE_DIRNAME", "$WEB_DIR/$SITE_DIRNAME")

?>
