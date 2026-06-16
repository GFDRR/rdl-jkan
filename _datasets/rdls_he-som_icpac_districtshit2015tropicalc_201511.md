---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-megh
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-megh
dataset_id: rdls_he-som_icpac_districtshit2015tropicalc_201511
description: '2015 TC Megh struck Berbera and Bossaso Districts in Somalia. The storm
  orignated from the Arabian Sea causing even more rains in parts of Bari region in
  Puntland and Somaliland. On November 9, 2015 just days after TC Chapala, TC Megh
  passed 57 km (36 mi) north of Cape Guardafui, Somalia, where it dropped heavy rainfall
  300% of the annual average. Eyl reported 160 mm (6.3 in) of rainfall over 24 hours.
  The villages hitted in the two districts included, Af Kalahay, Alula, Bareda, BiyoCade,
  Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo, Sayn Weyn, Sayn Yar, Toxin, Xaabo,
  Baargaal, Bander, Bareeda, Butiyaal, Caluula, Murcanyo, Qandalla, Xaabo and some
  parts of Xaafun, Biyacad, Bulahar, Ceelsheik and Shacable TC Megh damaged roads,
  crops, and schools. Re-estimated population figures after Tropical Megh, showed
  4.9 million people were in need of assistance, 308,700 children under-5 were acutely
  malnourished, of which 55,800 were severely malnourished and 1.1 million remain
  in a protracted internal displacement situation. Summary of impacts include: People
  affected: 132,000 People Displace: 3,000 Worst hit people: 800 Destroyed houses:
  1,129. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-megh]'
details: null
exposure:
- asset_type:
    description: Population in districts affected by TC Megh including Berbera, Bossaso,
      and villages in Bari region
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event spatial dataset documenting districts impacted by Tropical
    Cyclone Megh in November 2015, compiled by ICPAC from observed rainfall measurements
    (300% of annual average, 160 mm in 24 hours at Eyl) and affected settlement locations
    across Puntland and Somaliland regions.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-megh
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCMeg&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. 2015 TC Megh struck Berbera and Bossaso Districts
    in Somalia. The storm orignated from the Arabian Sea causing even more rains in
    parts of Bari region in Puntland and Somaliland. On November 9, 2015 just days
    after TC Chapala, TC Megh passed 57 km (36 mi) north of Cape Guardafui, Somalia,
    where it dropped heavy rainfall 300% of the annual average. Eyl reported 160 mm
    (6.3 in) of rainfall over 24 hours. The villages hitted in the two districts included,
    Af Kalahay, Alula, Bareda, BiyoCade, Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo,
    Sayn Weyn, Sayn Yar, Toxin, Xaabo, Baargaal, Bander, Bareeda, Butiyaal, Caluula,
    Murcanyo, Qandalla, Xaabo and some parts of Xaafun, Biyacad, Bulahar, Ceelsheik
    and Shacable
  download_url: null
  format: null
  id: resource_f76b80df
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Megh Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCMeg&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. 2015 TC Megh struck Berbera and Bossaso Districts in Somalia.
    The storm orignated from the Arabian Sea causing even more rains in parts of Bari
    region in Puntland and Somaliland. On November 9, 2015 just days after TC Chapala,
    TC Megh passed 57 km (36 mi) north of Cape Guardafui, Somalia, where it dropped
    heavy rainfall 300% of the annual average. Eyl reported 160 mm (6.3 in) of rainfall
    over 24 hours. The villages hitted in the two districts included, Af Kalahay,
    Alula, Bareda, BiyoCade, Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo, Sayn
    Weyn, Sayn Yar, Toxin, Xaabo, Baargaal, Bander, Bareeda, Butiyaal, Caluula, Murcanyo,
    Qandalla, Xaabo and some parts of Xaafun, Biyacad, Bulahar, Ceelsheik and Shacable
  download_url: null
  format: null
  id: resource_0f53f10e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Megh CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCMeg&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. 2015 TC Megh struck Berbera and Bossaso Districts in Somalia.
    The storm orignated from the Arabian Sea causing even more rains in parts of Bari
    region in Puntland and Somaliland. On November 9, 2015 just days after TC Chapala,
    TC Megh passed 57 km (36 mi) north of Cape Guardafui, Somalia, where it dropped
    heavy rainfall 300% of the annual average. Eyl reported 160 mm (6.3 in) of rainfall
    over 24 hours. The villages hitted in the two districts included, Af Kalahay,
    Alula, Bareda, BiyoCade, Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo, Sayn
    Weyn, Sayn Yar, Toxin, Xaabo, Baargaal, Bander, Bareeda, Butiyaal, Caluula, Murcanyo,
    Qandalla, Xaabo and some parts of Xaafun, Biyacad, Bulahar, Ceelsheik and Shacable
  download_url: null
  format: null
  id: resource_dd984b89
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Megh Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCMeg&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. 2015 TC Megh struck Berbera and Bossaso Districts in
    Somalia. The storm orignated from the Arabian Sea causing even more rains in parts
    of Bari region in Puntland and Somaliland. On November 9, 2015 just days after
    TC Chapala, TC Megh passed 57 km (36 mi) north of Cape Guardafui, Somalia, where
    it dropped heavy rainfall 300% of the annual average. Eyl reported 160 mm (6.3
    in) of rainfall over 24 hours. The villages hitted in the two districts included,
    Af Kalahay, Alula, Bareda, BiyoCade, Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo,
    Sayn Weyn, Sayn Yar, Toxin, Xaabo, Baargaal, Bander, Bareeda, Butiyaal, Caluula,
    Murcanyo, Qandalla, Xaabo and some parts of Xaafun, Biyacad, Bulahar, Ceelsheik
    and Shacable
  download_url: null
  format: null
  id: resource_c3986800
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Megh GeoJSON
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_icpac_districtshit2015tropicalc_201511
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-11-09'
  start: '2015-11-08'
temporal_resolution: null
title: Somalia Districts hit by 2015 Tropical Cyclone Megh
version: null
vulnerability: null
---
