clc; clear; close all; warning off all ;

buah = imread("buaah.jpg");
% figure, imshow(buah);


% mengkonversi citra rgb menjadi grayscale
buahtogray = double(rgb2gray(buah));
% figure, imshow(buahtogray, []);

%konvolusi dengan operator roberts 
robertshor = [0 1; - 1 0];
robertsver = [1 0; 0 -1];
Ix =  conv2(buahtogray, robertshor,'same');
Iy = conv2(buahtogray, robertsver, 'same');
J = sqrt((Ix.^2) + (Iy.^2));

% menampilkan citra hasil konvolusi
% figure, imshow(Ix, [])
% figure, imshow(Iy, [])
% figure, imshow(J, [])

% melakukan threesholidng citra untuk menghasilkan citra biner
K = uint8(J);
L = imbinarize(K, 0.08);
% figure, imshow(L);

% melakukan operasi morfologi 
M = imfill(L,'holes');
N = bwareaopen(M,10000);
% figure, imshow(M);
% figure, imshow(N);

%mengambil boudingx box masing-masing object
[labeled, numObjects] = bwlabel(N,8);
figure, imshow(labeled,[]);

stats = regionprops(labeled, "Boundingbox");
bbox = cat(1,stats.BoundingBox);

%menampilkan bounding box citra hasil segementasi
figure, imshow(buah);
hold on

for idx = 1:numObjects
    h = rectangle('Position',bbox(idx, :),'LineWidth', 2)
    set(h,'EdgeColor',[1 0 0]);
    hold on;
end
% menampilkan  jumlah objeck hasil segmentasi ;
title(["Jumlah Objek Ada:" ,num2str(numObjects)]);
hold off;
    