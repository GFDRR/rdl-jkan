---
attributions:
- entity:
    affiliation: null
    email: null
    name: CCCM Cluster Somalia IDP Site Verification
    url: https://data.humdata.org/dataset/somalia-idp-site-master-list-2nd-quarter-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: REACH Detailed Site Assessment (DSA)
    url: https://data.humdata.org/dataset/somalia-idp-site-master-list-2nd-quarter-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: CCCM Cluster Somalia
  url: https://data.humdata.org/dataset/somalia-idp-site-master-list-2nd-quarter-2022
creator:
  affiliation: null
  email: null
  name: CCCM Cluster Somalia
  url: https://data.humdata.org/dataset/somalia-idp-site-master-list-2nd-quarter-2022
dataset_id: rdls_el-som_cccmsom_listidpsites
description: 'The updated master list of IDP sites contains estimated population data,
  GPS coordinates, names of neighborhoods/umbrellas (sub-district locations) and unique
  codes for each verified site. Additionally, the Q1-2023 master list includes IDP
  sites/populations for proposed catchment areas located in Baidoa and Mogadishu to
  better enable the formulation of an area-based approach to humanitarian service
  delivery. When possible, the CCCM Cluster urges partners to ensure that the names
  of IDP sites used by agencies are matching with that of the CCCM Cluster''s IDP
  Site Master List.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-idp-site-master-list-2nd-quarter-2022]'
details: null
exposure:
- asset_type:
    description: Internally displaced population enumerated at verified IDP sites
      across Somalia
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDP site master lists were compiled through direct observational data
    collection and anecdotal reporting by the CCCM Cluster Somalia and REACH, with
    site verification, GPS coordinate collection, and population enumeration. Data
    were aggregated into quarterly master lists with standardized site names, neighborhood
    classifications, and catchment area designations to support area-based humanitarian
    service delivery planning.
  sources:
  - id: source_1
    license: null
    name: CCCM Cluster Somalia IDP Site Verification
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: REACH Detailed Site Assessment (DSA)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-idp-site-master-list-2nd-quarter-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population counts at IDP sites in Somalia
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
        metric: displaced
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
  description: 'CCCM Cluster Somalia: List of IDP sites in Somalia (List of Verified
    IDP sites in Somalia updated as of July 2023)'
  download_url: https://data.humdata.org/dataset/bca5fd46-5e2d-4ca2-9321-6e2961fbb9e8/resource/d88b655c-6c94-4682-a401-971d0f98b79f/download/idp-site-master-list-2nd-quarter-2023.xlsx
  format: null
  id: resource_d88b655c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP Site Master List - 2nd Quarter 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'CCCM Cluster Somalia: List of IDP sites in Somalia (List of Verified
    IDP sites in Somalia updated as of March 2023)'
  download_url: https://data.humdata.org/dataset/bca5fd46-5e2d-4ca2-9321-6e2961fbb9e8/resource/7dce0de5-ccfb-47b2-83a1-6fd12a93646f/download/idp-site-master-list-1st-quarter-2023.xlsx
  format: null
  id: resource_7dce0de5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP Site Master List - 1st Quarter 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'CCCM Cluster Somalia: List of IDP sites in Somalia (List of Verified
    IDP sites in Somalia updated as of October 2022)'
  download_url: https://data.humdata.org/dataset/bca5fd46-5e2d-4ca2-9321-6e2961fbb9e8/resource/daca964a-40be-4d38-bc59-a8895ef2a71c/download/idp-site-master-list-3rd-quarter-2022.xlsx
  format: null
  id: resource_daca964a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP Site Master List - 3rd Quarter 2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'CCCM Cluster Somalia: List of IDP sites in Somalia (List of Verified
    IDP sites in Somalia updated as of June 2022)'
  download_url: https://data.humdata.org/dataset/bca5fd46-5e2d-4ca2-9321-6e2961fbb9e8/resource/5901058d-3bdb-4707-adc8-98145bcd58f4/download/idp-site-master-list-2nd-quarter-2022.xlsx
  format: null
  id: resource_5901058d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP Site Master List - 2nd Quarter 2022.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_cccmsom_listidpsites
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: 'CCCM Cluster Somalia: List of IDP sites in Somalia'
version: null
vulnerability: null
---
