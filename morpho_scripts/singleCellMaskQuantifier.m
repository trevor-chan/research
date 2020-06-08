%mask = imread('maskimages/3bef101b5cc043ab463b2b5e256485287227d853bbd6a6e4079f957ed89f5166.png');
mask = imread('maskimages/317be41937da7258682bb36e889d486498d055bcf83f2c144a8f89393dcddaad.png');
%read in image folder, give all properties

stats = regionprops(mask,'Area','BoundingBox','Centroid',...
    'MajorAxisLength','MinorAxisLength','Circularity','Eccentricity',...
    'Orientation');

area = cat(1,stats.Area);
centroids = cat(1,stats.Centroid);
circularity = cat(1,stats.Circularity);
eccentricity = cat(1,stats.Eccentricity);
orientation = cat(1,stats.Orientation);

imshow(mask)
hold on
plot(centroids(:,1),centroids(:,2),'r.')
hold off

