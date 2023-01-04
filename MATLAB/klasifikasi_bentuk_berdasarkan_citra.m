clc; clear; close all; warning off all;

% membaca citra rgb

A = imread("gg.jpg");
figure, imshow(A);

%mengkonversi citra rgb menjadi grayscale

B = rgb2gray(A);
figure, imshow(B);

%melakukan operasi thresholding //segmentasi citra memisahkan background
%objek

C = imbinarize(B);
figure, imshow(C);

%melakukan operasi komplemen 
D = imcomplement(C);
figure, imshow(D);

%melakukan operasi morfologi fillings hole (mengisi lubang-lubang hitam
%menjadi warna putih pada sebuah objek).
E = imfill(D,'holes');
figure, imshow(E);

%melakukan pelablen // memberikan pengurutan dari sebuah objeck
%
[labeled,numObjects] = bwlabel(E);
figure, imshow(labeled,[]);
labeledrgb = label2rgb(E);
figure, imshow(labeledrgb, [])

%melakukan ekstraksi fitur pada masing-masing objek

s = regionprops(labeled, 'Area','Perimeter','BoundingBox');
luas =  cat(1,s.Area);
keliling = cat(1,s.Perimeter);
bbox = cat(1,s.BoundingBox);
metric = 4*pi * luas./(keliling.^2);


% klasifikasi bentuk pada masing-masing objeck
for k =1:numObjects
    if metric(k)>0.7
        A = insertObjectAnnotation(A,'rectangle',bbox(k,:),'Mur',...
            'LineWidth',3,'Color','y','FontSize',24);
    else 
        A = insertObjectAnnotation(A,'rectangle',bbox(k,:),'Baut',...
            'LineWidth',3,'Color','y','FontSize',24);
    end
end

% menampilkan citra hasil kalsifikasi
figure, imshow(A);
