---
attributions:
- entity:
    affiliation: null
    email: null
    name: IGAD Climate Prediction and Applications Centre (ICPAC)
    url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-chapala
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-chapala
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-chapala
dataset_id: rdls_hl-som_icpac_districtshit2015tropicalc_201511
description: 'This layer show two Somalia Districts struck by 2015 Tropical Cyclone
  Chapala, Berbera and Bossaso Districts. On November 2, 2015 TC Chapala entered the
  Gulf of Aden in Somalia as the strongest tropical cyclone on record. 2015 TC Chapala
  prduced maximum wind speeds of 130knots. It brought rainfall in Northern Bari Region
  in Bossaso Districts. The villages struck within the recorded districts include,
  Baargaal, Bander, Bareeda, Butiyaal, Caluula, Murcanyo, Qandalla, Xaabo, Biycad,
  Bulahar, Ceelsheik, Shacable, Xaafun. According to a joint inter-agency rapid assessment
  more than 500 families (4,000 people) were affected by Tropical Cyclones Chapala
  and Megh, most affected lived in Gardaful Region, Puntland. No human loss of life
  was reported, but the rainfall and waves destroyed people&rsquo;s homes, washed
  fishing boats and nets, killed livestock (an estimated 3,000 sheep and goats, as
  well as 200 camels) and caused damage/destruction to public infrastructure including
  hospitals, roads and schools. It was estimated that 4,000 people had been displaced,
  with 1,129 people being worst affected, having lost their homes and livelihoods
  (business, fishing boats, engines and nets), which were swept away by waves. It
  was reported that there had been extensive damage/destruction to people&rsquo;s
  livelihoods, with 80 per cent of villages in Alula and 60 per cent of villages in
  Af Kalahay Bareda, BiyoCade, Boolimoog, Dhurbo, Fagoora, Geesalay, Murcanyo, Murcanyo,
  Sayn Weyn, Sayn Yar, Toxiin and Xaabo experiencing loss of livestock and damage
  to crops and fisheries.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-chapala]'
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Post-event assessment data from joint inter-agency rapid appraisal
    documenting the geographic extent and population impact of 2015 Tropical Cyclone
    Chapala in Somalia. District-level administrative boundaries were overlaid with
    cyclone impact zones to identify affected areas and quantify affected population
    counts.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Centre (ICPAC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2015-tropical-cyclone-chapala
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population (500+ families) from 2015 Tropical Cyclone Chapala
      in Somalia districts
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCChapal&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer show two Somalia Districts struck
    by 2015 Tropical Cyclone Chapala, Berbera and Bossaso Districts. On November 2,
    2015 TC Chapala entered the Gulf of Aden in Somalia as the strongest tropical
    cyclone on record. 2015 TC Chapala prduced maximum wind speeds of 130knots. It
    brought rainfall in Northern Bari Region in Bossaso Districts. The villages struck
    within the recorded districts include, Baargaal, Bander, Bareeda, Butiyaal, Caluula,
    Murcanyo, Qandalla, Xaabo, Biycad, Bulahar, Ceelsheik, Shacable, Xaafun.
  download_url: null
  format: null
  id: resource_b4a325cf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Chapala Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCChapal&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer show two Somalia Districts struck by 2015 Tropical
    Cyclone Chapala, Berbera and Bossaso Districts. On November 2, 2015 TC Chapala
    entered the Gulf of Aden in Somalia as the strongest tropical cyclone on record.
    2015 TC Chapala prduced maximum wind speeds of 130knots. It brought rainfall in
    Northern Bari Region in Bossaso Districts. The villages struck within the recorded
    districts include, Baargaal, Bander, Bareeda, Butiyaal, Caluula, Murcanyo, Qandalla,
    Xaabo, Biycad, Bulahar, Ceelsheik, Shacable, Xaafun.
  download_url: null
  format: null
  id: resource_c69f5bd1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Chapala CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCChapal&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer show two Somalia Districts struck by 2015 Tropical
    Cyclone Chapala, Berbera and Bossaso Districts. On November 2, 2015 TC Chapala
    entered the Gulf of Aden in Somalia as the strongest tropical cyclone on record.
    2015 TC Chapala prduced maximum wind speeds of 130knots. It brought rainfall in
    Northern Bari Region in Bossaso Districts. The villages struck within the recorded
    districts include, Baargaal, Bander, Bareeda, Butiyaal, Caluula, Murcanyo, Qandalla,
    Xaabo, Biycad, Bulahar, Ceelsheik, Shacable, Xaafun.
  download_url: null
  format: null
  id: resource_82d47210
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Chapala Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2015_TCChapal&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer show two Somalia Districts struck by 2015
    Tropical Cyclone Chapala, Berbera and Bossaso Districts. On November 2, 2015 TC
    Chapala entered the Gulf of Aden in Somalia as the strongest tropical cyclone
    on record. 2015 TC Chapala prduced maximum wind speeds of 130knots. It brought
    rainfall in Northern Bari Region in Bossaso Districts. The villages struck within
    the recorded districts include, Baargaal, Bander, Bareeda, Butiyaal, Caluula,
    Murcanyo, Qandalla, Xaabo, Biycad, Bulahar, Ceelsheik, Shacable, Xaafun.
  download_url: null
  format: null
  id: resource_f136aa45
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2015 Tropical Cyclone Chapala GeoJSON
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_icpac_districtshit2015tropicalc_201511
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
  end: '2015-11-06'
  start: '2015-11-02'
temporal_resolution: null
title: Somalia Districts hit by 2015 Tropical Cyclone Chapala
version: null
vulnerability: null
---
