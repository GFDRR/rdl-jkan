---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-chapala-path
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-chapala-path
dataset_id: rdls_hl-somyem_icpac_2015tropicalcyclonechapal_201511
description: 'This layer shows the movement path of 2015 Tropical Cyclone Chapala.
  On Monday 2 November 2015, Tropical Cyclone Chapala made a landfall in Yemen; however,
  its effects were also felt across the Gulf of Aden in Somalia where extensive rainfall
  was experienced in the Northern Bari region in Bosaso district, Puntland. The storm
  reached maximum wind speed of 130knots. According to a joint inter-agency rapid
  assessment more than 500 families (4,000 people) were affected by Tropical Cyclones
  Chapala and Megh, most affected lived in Gardaful Region, Puntland. No human loss
  of life was reported, but the rainfall and waves destroyed people&rsquo;s homes,
  washed fishing boats and nets, killed livestock (an estimated 3,000 sheep and goats,
  as well as 200 camels) and caused damage/destruction to public infrastructure including
  hospitals, roads and schools. It was also estimated that 4,000 people were displaced,
  with 1,129 people being worst affected, having lost their homes and livelihoods
  (business, fishing boats, engines and nets), which were swept away by waves. It
  was reported that there had been extensive damage/destruction to people&rsquo;s
  livelihoods, with 80 per cent of villages in Alula and 60 per cent of villages in
  Af Kalahay Bareda, BiyoCade, Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo, Murcanyo,
  Sayn Weyn, Sayn Yar, Toxiin and Xaabo experiencing loss of livestock and damage
  to crops and fisheries.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-chapala-path]'
details: null
exposure: []
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
  description: Observed tropical cyclone track data collected and compiled by ICPAC
    documenting the movement path, position, and meteorological characteristics of
    Tropical Cyclone Chapala from November 2015, with associated impact reports from
    rapid inter-agency assessments in affected regions of Yemen and Somalia.
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
- href: https://data.humdata.org/dataset/icpac-geonode-2015-tropical-cyclone-chapala-path
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Tropical Cyclone Chapala in Yemen and Somalia
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
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala0&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer shows the movement path of 2015 Tropical Cyclone
    Chapala. On Monday 2 November 2015, Tropical Cyclone Chapala made a landfall in
    Yemen; however, its effects were also felt across the Gulf of Aden in Somalia
    where extensive rainfall was experienced in the Northern Bari region in Bosaso
    district, Puntland. The storm reached maximum wind speed of 130knots.
  download_url: null
  format: null
  id: resource_6becee34
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Chapala Path Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala0&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer shows the movement path of 2015 Tropical
    Cyclone Chapala. On Monday 2 November 2015, Tropical Cyclone Chapala made a landfall
    in Yemen; however, its effects were also felt across the Gulf of Aden in Somalia
    where extensive rainfall was experienced in the Northern Bari region in Bosaso
    district, Puntland. The storm reached maximum wind speed of 130knots.
  download_url: null
  format: null
  id: resource_d4a0dcbe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Chapala Path Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala0&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer shows the movement path of 2015 Tropical Cyclone
    Chapala. On Monday 2 November 2015, Tropical Cyclone Chapala made a landfall in
    Yemen; however, its effects were also felt across the Gulf of Aden in Somalia
    where extensive rainfall was experienced in the Northern Bari region in Bosaso
    district, Puntland. The storm reached maximum wind speed of 130knots.
  download_url: null
  format: null
  id: resource_8a53e422
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Chapala Path CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TC_Chapala0&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer shows the movement path of 2015 Tropical Cyclone
    Chapala. On Monday 2 November 2015, Tropical Cyclone Chapala made a landfall in
    Yemen; however, its effects were also felt across the Gulf of Aden in Somalia
    where extensive rainfall was experienced in the Northern Bari region in Bosaso
    district, Puntland. The storm reached maximum wind speed of 130knots.
  download_url: null
  format: null
  id: resource_77261f03
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2015 Tropical Cyclone Chapala Path GeoJSON
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-somyem_icpac_2015tropicalcyclonechapal_201511
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  - SOM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-11-06'
  start: '2015-11-02'
temporal_resolution: null
title: 2015 Tropical Cyclone Chapala Path
version: null
vulnerability: null
---
