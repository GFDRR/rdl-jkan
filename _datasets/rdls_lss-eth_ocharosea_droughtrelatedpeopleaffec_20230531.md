---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/ethiopia-pin-targeted-reached-by-location-and-cluster
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/ethiopia-pin-targeted-reached-by-location-and-cluster
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/ethiopia-pin-targeted-reached-by-location-and-cluster
dataset_id: rdls_lss-eth_ocharosea_droughtrelatedpeopleaffec_20230531
description: 'Drought affected areas and population in Ethiopia. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ethiopia-pin-targeted-reached-by-location-and-cluster]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Humanitarian partners compiled drought impact data on affected populations,
    targeted beneficiaries, and reached populations across Ethiopia by geographic
    location. The dataset aggregates field reports and administrative records from
    multiple organizations responding to drought emergencies, providing spatial distribution
    of drought impacts and humanitarian response coverage.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-pin-targeted-reached-by-location-and-cluster
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by drought in Ethiopia by location
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
  - asset_category: population
    asset_dimension: population
    description: Population targeted for humanitarian assistance due to drought
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
  - asset_category: population
    asset_dimension: population
    description: Population reached by humanitarian assistance in drought-affected
      areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
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
  url: https://reliefweb.int/updates?advanced-search=(PC87
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia Drought Related - People Affected, Targeted & Reached by Location
    (CSV)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vRppQx8JTKkKRCKmzfnCMmTFEcvCpkbP9PdHs1sQTUyacmbsx8tlAXpgBLFce-lcehukreGGuXjA_4S/pub?gid=1428130716&single=true&output=csv
  format: null
  id: resource_27469ccb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ethiopia-drought-affected-targeted-reached-by-location
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ocharosea_droughtrelatedpeopleaffec_20230531
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
  start: '2023-05-31'
temporal_resolution: null
title: Ethiopia Drought Related - People Affected, Targeted & Reached by Location
version: null
vulnerability: null
---
