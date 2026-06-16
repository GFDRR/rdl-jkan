---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2015-tropical-cyclone-chapala
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2015-tropical-cyclone-chapala
dataset_id: rdls_hl-som_icpac_regionshit2015tropicalcyc_201511
description: 'On November 2, 2015 Cyclone Chapala entered the Gulf of Aden as the
  strongest tropical cyclone on record. The storm dropped heavy rainfall in Puntland
  and Somaliland. This layer shows the occurence of TC Chapala in two Somalia regions:
  Bari and Woqooyi Galbeed Provinces. TC Chapala first made a landfall in Yemen; however,
  its effects were also felt across the Gulf of Aden in Somalia where extensive rainfall
  was experienced in the Northern Bari region in Bosaso district, Puntland. TC Chapala
  was characterized by heavy rainfall that had adverse impacts in the regions. It
  resulted to death of over 25,000 animals and left thousands of people homeless,
  leaving some local nomadic tribes without any food. Impacts recorded included: Number
  of people affected: up to 80% of the population. Number of people worst hit: 500
  families(4000ppl) Number of people displaced: 4000 Livestock destroyed: 3,000 sheep
  and goats and 200 camels. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2015-tropical-cyclone-chapala]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
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
license: CC-BY-4.0
lineage:
  description: Post-event spatial mapping of regions affected by Tropical Cyclone
    Chapala in November 2015, documenting the cyclone's occurrence and associated
    heavy rainfall impacts in Puntland and Somaliland regions of Somalia.
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
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-regions-hit-by-2015-tropical-cyclone-chapala
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities resulting from Tropical Cyclone Chapala impacts in Somalia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Excel file. On November 2, 2015 Cyclone Chapala entered the Gulf of
    Aden as the strongest tropical cyclone on record. The storm dropped heavy rainfall
    in Puntland and Somaliland. This layer shows the occurence of TC Chapala in two
    Somalia regions: Bari and Woqooyi Galbeed Provinces. TC Chapala first made a landfall
    in Yemen; however, its effects were also felt across the Gulf of Aden in Somalia
    where extensive rainfall was experienced in the Northern Bari region in Bosaso
    district, Puntland.'
  download_url: null
  format: null
  id: resource_b2df8a4e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2015 Tropical Cyclone Chapala Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'GeoJSON file. On November 2, 2015 Cyclone Chapala entered the Gulf
    of Aden as the strongest tropical cyclone on record. The storm dropped heavy rainfall
    in Puntland and Somaliland. This layer shows the occurence of TC Chapala in two
    Somalia regions: Bari and Woqooyi Galbeed Provinces. TC Chapala first made a landfall
    in Yemen; however, its effects were also felt across the Gulf of Aden in Somalia
    where extensive rainfall was experienced in the Northern Bari region in Bosaso
    district, Puntland.'
  download_url: null
  format: null
  id: resource_27e4a648
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2015 Tropical Cyclone Chapala GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'Zipped Shapefile file. On November 2, 2015 Cyclone Chapala entered
    the Gulf of Aden as the strongest tropical cyclone on record. The storm dropped
    heavy rainfall in Puntland and Somaliland. This layer shows the occurence of TC
    Chapala in two Somalia regions: Bari and Woqooyi Galbeed Provinces. TC Chapala
    first made a landfall in Yemen; however, its effects were also felt across the
    Gulf of Aden in Somalia where extensive rainfall was experienced in the Northern
    Bari region in Bosaso district, Puntland.'
  download_url: null
  format: null
  id: resource_1d31d4bf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2015 Tropical Cyclone Chapala Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: 'CSV file. On November 2, 2015 Cyclone Chapala entered the Gulf of
    Aden as the strongest tropical cyclone on record. The storm dropped heavy rainfall
    in Puntland and Somaliland. This layer shows the occurence of TC Chapala in two
    Somalia regions: Bari and Woqooyi Galbeed Provinces. TC Chapala first made a landfall
    in Yemen; however, its effects were also felt across the Gulf of Aden in Somalia
    where extensive rainfall was experienced in the Northern Bari region in Bosaso
    district, Puntland.'
  download_url: null
  format: null
  id: resource_55ae065e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Regions hit by 2015 Tropical Cyclone Chapala CSV
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_regionshit2015tropicalcyc_201511
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
  end: '2015-11-05'
  start: '2015-11-02'
temporal_resolution: null
title: Somalia Regions hit by 2015 Tropical Cyclone Chapala
version: null
vulnerability: null
---
