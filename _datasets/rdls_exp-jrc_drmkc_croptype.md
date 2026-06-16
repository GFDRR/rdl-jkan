---
attributions:
- entity:
    affiliation: null
    email: jrc-risk-data-hub@ec.europa.eu
    name: European Commision (EC), Joint Research Centre (JRC)
    url: https://joint-research-centre.ec.europa.eu/
  id: Entity_1
  role: resource_provider
- entity:
    affiliation: null
    email: null
    name: University of Natural Resources and Life Sciences, vienna
    url: https://boku.ac.at/en/
  id: Entity_2
  role: contributor
catalog: null
contact_point:
  affiliation: null
  email: marijn.van-der-velde@ec.europa.eu
  name: Marijn van der Velde
  url: https://joint-research-centre.ec.europa.eu/
creator:
  affiliation: null
  email: null
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
- asset_type: null
  category: agriculture
  id: exp_1
  metrics:
  - dimension: content
    id: crop_type
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type: null
    type: model
    url: https://data.jrc.ec.europa.eu/dataset/555e5d1d-1aae-4320-a716-2e6d18aa1e7c
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: 'EUCROPMAP : European Union Crop type Map'
  url: https://data.jrc.ec.europa.eu/dataset/555e5d1d-1aae-4320-a716-2e6d18aa1e7c
publisher:
  affiliation: null
  email: null
  name: European Commission, Joint Research Centre
  url: https://joint-research-centre.ec.europa.eu/
purpose: To provide detailed 10-metre resolution crop type mapping for EU-27 and Ukraine
  using satellite imagery and machine learning to support agricultural monitoring,
  land use planning, and policy development.
referenced_by:
- author_names:
  - Babak Ghassemi
  - Emma Izquierdo-Verdiguier
  - Astrid Verhegghen
  - Momchil Yordanov
  - Guido Lemoine
  - "\xC1lvaro Moreno Mart\xEDnez"
  - Davide De Marchi
  - Marijn van der Velde
  - Francesco Vuolo
  - "Rapha\xEBl d\u2019Andrimont"
  date_published: '2024-09-27'
  doi: https://doi.org/10.1038/s41597-024-03884-y
  id: Ref_1
  name: "European Union crop map 2022: Earth observation\u2019s 10-meter dive into\
    \ Europe\u2019s crop tapestry"
  url: https://publications.jrc.ec.europa.eu/repository/handle/JRC136054
resources:
- access_url: https://data.jrc.ec.europa.eu/dataset/555e5d1d-1aae-4320-a716-2e6d18aa1e7c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Derived from multi-temporal satellite observations (e.g., Sentinel-1/2)
    and ancillary data to map dominant crop classes at high resolution. Suitable for
    agricultural monitoring, statistics, and modeling across EU member states.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EUCROPMAP/2022/EU_CropMap_22_v1_stratum_EU27-HR.tif
  format: null
  id: EuCropMap_2022_EU-27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10
  temporal:
    central_year: null
    duration: null
    end: '2022-12-31'
    start: '2022-01-01'
  temporal_resolution: null
  title: EuCropMap 2022 EU-27 Pixel-level crop type classification for the EU-27 for
    the 2022 growing season.
- access_url: https://data.jrc.ec.europa.eu/dataset/555e5d1d-1aae-4320-a716-2e6d18aa1e7c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Produced from multi-temporal satellite observations and ancillary inputs
    to identify dominant crop classes at high resolution. Supports national/regional
    agricultural assessments and spatial analyses.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EUCROPMAP/2022/EU_CropMap_22_v1_stratum_UA-HR.tif
  format: null
  id: EuCropMap_2022_Ukraine
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10
  temporal:
    central_year: null
    duration: null
    end: '2022-12-31'
    start: '2022-01-01'
  temporal_resolution: null
  title: EuCropMap 2022 Ukraine Pixel-level crop type map for Ukraine for the 2022
    growing season.
- access_url: https://data.jrc.ec.europa.eu/dataset/555e5d1d-1aae-4320-a716-2e6d18aa1e7c
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: QGIS style file (.qml) providing the official color palette and class
    labels for EUCROPMAP 2022 crop classes.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EUCROPMAP/2022/EuroCropMap2022.qml
  format: null
  id: qgis_layer_style
  media_type: application/xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal:
    central_year: null
    duration: null
    end: '2022-12-31'
    start: '2022-01-01'
  temporal_resolution: null
  title: Legend of EU crop map 2022 (colour and label) in QML
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_drmkc_croptype
spatial:
  bbox: null
  centroid: null
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
spatial_resolution: null
temporal: null
temporal_resolution: null
title: European Union Crop type Map 2022
version: '2023'
vulnerability: null
---
