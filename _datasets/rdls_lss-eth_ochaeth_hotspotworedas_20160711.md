---
attributions:
- entity:
    affiliation: null
    email: null
    name: Emergency Nutrition Coordination Unit (ENCU)
    url: https://data.humdata.org/dataset/hotspot-woredas
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/hotspot-woredas
creator:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/hotspot-woredas
dataset_id: rdls_lss-eth_ochaeth_hotspotworedas_20160711
description: 'Hotspot woreda classification is derived using six multisector indicators,
  including agriculture and nutrition, agreed at regional and federal levels. A hotspot
  matrix is often used as a proxy for the acute Integrated Phase Food Security Classification
  (IPC) and is indicative of food security and nutrition status. Hotspot woredas require
  urgent humanitarian response.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotspot-woredas]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Hotspot woreda classification derived from six multisector indicators
    (agriculture, nutrition, and others) agreed at regional and federal levels. The
    hotspot matrix serves as a proxy for acute Integrated Phase Food Security Classification
    (IPC) to identify areas with critical food security and nutrition status requiring
    urgent humanitarian intervention.
  sources:
  - id: source_1
    license: null
    name: Emergency Nutrition Coordination Unit (ENCU)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotspot-woredas
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity and nutrition vulnerability classification in drought-affected
      woredas
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
          quantity_kind: area
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Hotspot woreda classification is derived using six multisector indicators,
    including agriculture and nutrition, agreed at regional and federal levels. A
    hotspot matrix is often used as a proxy for the acute Integrated Phase Food Security
    Classification (IPC) and is indicative of food security and nutrition status.
    Hotspot woredas require urgent humanitarian response.
  download_url: https://data.humdata.org/dataset/76029294-3cbc-4bd0-8786-adcdb6475886/resource/de8995a4-a792-4260-a842-cefe744f0d35/download/ethiopia-hotspot-woredas-july2016.xls
  format: null
  id: resource_de8995a4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia-Hotspot Woredas-July2016.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ochaeth_hotspotworedas_20160711
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-07-11'
temporal_resolution: null
title: Ethiopia - Hotspot Woredas
version: null
vulnerability: null
---
