. set-webapp-path.sh
rm -rf $WEBAPP_PATH/dist
npm run build --prefix $WEBAPP_PATH
git rm -rf css js
rm -rf css js
cp -R ~/WebstormProjects/aws-on-leaflet/dist/* .
git add css js
