---
attributions:
- entity:
    affiliation: null
    email: null
    name: BNPB
    url: https://data.humdata.org/dataset/village-affected-by-flood-in-west-java-province
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: BPS-Statistics Indonesia
    url: https://data.humdata.org/dataset/village-affected-by-flood-in-west-java-province
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/village-affected-by-flood-in-west-java-province
creator:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/village-affected-by-flood-in-west-java-province
dataset_id: rdls_lss-idn_unfpaidn_villageaffectedfloodwestj_20200114
description: 'Village affected by flood in Bogor and Lebak District - West Java Province
  on January 2020, the data source from BNPB, admin boundaries from BPS-Statistics
  Indonesia, 2016. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/village-affected-by-flood-in-west-java-province]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Village-level flood impact data collected through direct observation
    by BNPB during the January 2020 flood event in Bogor and Lebak districts, West
    Java. Administrative boundaries from BPS-Statistics Indonesia (2016) were used
    to spatially delineate affected villages. The dataset represents post-event impact
    records at the village administrative unit level.
  sources:
  - id: source_1
    license: null
    name: BNPB
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: BPS-Statistics Indonesia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/village-affected-by-flood-in-west-java-province
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Villages affected by flooding in Bogor and Lebak districts during
      January 2020 flood event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Village affected by flood in Bogor District - West Java Province on
    January 2020, the data source from BNPB, admin boundaries from BPS-Statistics
    Indonesia, 2016
  download_url: https://data.humdata.org/dataset/39ff9d88-db28-4737-bef9-05a4b1c89e02/resource/ea3a049d-2612-4c11-834d-79fdf6b50afb/download/desa_terdampak_bogor.zip
  format: null
  id: resource_ea3a049d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desa_terdampak_Bogor.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Village affected by flood in Lebak District - West Java Province on
    January 2020, West Java Province, data source from BNPB, admin boundaries from
    BPS-Statistics Indonesia, 2016
  download_url: https://data.humdata.org/dataset/39ff9d88-db28-4737-bef9-05a4b1c89e02/resource/7e31b42b-f15a-4e0e-ae8a-e432142a4604/download/desa_terdampak_lebak.zip
  format: null
  id: resource_7e31b42b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desa_Terdampak_Lebak.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idn_unfpaidn_villageaffectedfloodwestj_20200114
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-01-14'
temporal_resolution: null
title: Indonesia - Village affected by Flood, in West Java Province
version: null
vulnerability: null
---
