---
contact_point:
  email: marijn.van-der-velde@ec.europa.eu
  name: Marijn van der Velde
  url: https://joint-research-centre.ec.europa.eu/
creator:
  name: European Commission, Joint Research Centre
  url: https://joint-research-centre.ec.europa.eu/
dataset_id: rdls_exp-jrc_drmkc_croptype
description: Crop type map of the year 2022 covering EU-27 and Ukraine
details: "To provide the information needed for a detailed monitoring of crop types\
  \ across the European Union (EU), we present an advanced 10-metre resolution map\
  \ for the EU and Ukraine with 19 crop types for 2022, updating the 2018 version.\
  \ Using Earth Observation (EO) and in-situ data from Eurostat\u2019s Land Use and\
  \ Coverage Area Frame Survey (LUCAS) 2022, the methodology included 134,684 LUCAS\
  \ Copernicus polygons, Sentinel-1 and Sentinel-2 satellite imagery, land surface\
  \ temperature and a digital elevation model. Based on this data, two classification\
  \ layers were developed using a Random Forest machine learning approach: a primary\
  \ map and a gap-filling map to address cloud-covered gaps. The combined maps, covering\
  \ 27 EU countries, show an overall accuracy of 79.3% for seven major land cover\
  \ classes and 70.6% for all 19 crop types. The trained model was used to derive\
  \ the 2022 map for Ukraine, demonstrating its robustness even in regions without\
  \ labelled samples for model training."
exposure:
  category: agriculture
  dimension: content
  quantity_kind: area
  taxonomy: null
hazard: null
license: CC-BY-SA-4.0
loss: null
project: 'EUCROPMAP : European Union Crop type Map '
publisher:
  name: European Commission, Joint Research Centre
  url: https://joint-research-centre.ec.europa.eu/
purpose: To provide detailed 10-metre resolution crop type mapping for EU-27 and Ukraine
  using satellite imagery and machine learning to support agricultural monitoring,
  land use planning, and policy development.
resources:
- coordinate_system: EPSG:4326
  description: Derived from multi-temporal satellite observations (e.g., Sentinel-1/2)
    and ancillary data to map dominant crop classes at high resolution. Suitable for
    agricultural monitoring, statistics, and modeling across EU member states.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EUCROPMAP/2022/EU_CropMap_22_v1_stratum_EU27-HR.tif
  format: geotiff
  id: EuCropMap_2022_EU-27
  spatial_resolution: 10
  title: EuCropMap 2022 EU-27 Pixel-level crop type classification for the EU-27 for
    the 2022 growing season.
- coordinate_system: EPSG:4326
  description: Produced from multi-temporal satellite observations and ancillary inputs
    to identify dominant crop classes at high resolution. Supports national/regional
    agricultural assessments and spatial analyses.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EUCROPMAP/2022/EU_CropMap_22_v1_stratum_UA-HR.tif
  format: geotiff
  id: EuCropMap_2022_Ukraine
  spatial_resolution: 10
  title: EuCropMap 2022 Ukraine Pixel-level crop type map for Ukraine for the 2022
    growing season.
- coordinate_system: null
  description: QGIS style file (.qml) providing the official color palette and class
    labels for EUCROPMAP 2022 crop classes.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EUCROPMAP/2022/EuroCropMap2022.qml
  format: website
  id: qgis_layer_style
  spatial_resolution: null
  title: Legend of EU crop map 2022 (colour and label) in QML
risk_data_type:
- exposure
schema: rdl-02
slug: rdls_exp-jrc_drmkc_croptype
spatial:
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
title: European Union Crop type Map 2022
version: '2023'
vulnerability: null
---
