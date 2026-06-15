---
attributions:
- entity:
    affiliation: null
    email: null
    name: FSNWG (Food Security and Nutrition Working Group)
    url: https://data.humdata.org/dataset/eastern-africa-region-food-security-statistics-2010-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/eastern-africa-region-food-security-statistics-2010-2015
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/eastern-africa-region-food-security-statistics-2010-2015
dataset_id: rdls_lss-ocharosea_regionfoodsecuritystatist_20260924
description: 'Aggregated data on food insecure population in Kenya, Ethiopia, Uganda,
  Sudan, South Sudan, Rwanda, Burundi, Djibouti and Somalia from Dec 2010 to Jan 2015.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/eastern-africa-region-food-security-statistics-2010-2015]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Food security statistics were aggregated from FSNWG quarterly reports
    covering nine Eastern African countries from December 2010 to January 2015. Data
    represents post-event and ongoing food insecurity impact assessments compiled
    from regional humanitarian assessments, with spatial assumptions documented in
    accompanying shapefile.
  sources:
  - id: source_1
    license: null
    name: FSNWG (Food Security and Nutrition Working Group)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/eastern-africa-region-food-security-statistics-2010-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population affected by drought and food security crises
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://www.disasterriskreduction.net/east-central-africa/fsnwg
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Food insecure population statistics for the Horn of Africa (Eastern
    Africa region)
  download_url: https://data.humdata.org/dataset/2693d7e4-7e08-449d-aa22-7874a58f9f75/resource/67737c61-4aff-4661-9585-7192a08ad7d4/download/ea-food-security-stats-to-date-09mar2015.csv
  format: null
  id: resource_67737c61
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EA_Food Security Stats to date_09Mar2015.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Eastern Africa Region Food Security Statistics 2010 - 2015 (from FEWSNET)
  download_url: http://shapefiles.fews.net/east-africa201504.zip
  format: null
  id: resource_20809e84
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Assumptions for Quarterly Food Security Analysis
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ocharosea_regionfoodsecuritystatist_20260924
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  - ETH
  - UGA
  - SDN
  - SSD
  - RWA
  - BDI
  - DJI
  - SOM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-09-24'
temporal_resolution: null
title: Eastern Africa Region Food Security Statistics 2010 - 2015
version: null
vulnerability: null
---
