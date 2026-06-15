---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM Severity Index
    url: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ACAPS Humanitarian Access
    url: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian Access Events Dataset
    url: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Protection Monitoring Dataset
    url: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: ACAPS
  url: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package
creator:
  affiliation: null
  email: null
  name: ACAPS
  url: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package
dataset_id: rdls_lss-syrtur_acaps_earthquakedatapackage_20220301
description: 'This is a collection of all the available data on Turkiye and Syria
  in the ACAPS database as of 10.02.2023. The collection puts together the extraction
  of data from the following datasets and products: INFORM Severity Index (TUR005,
  SYR002, REG015 crises) ACAPS Humanitarian Access (TUR005, SYR002, REG015) Humanitarian
  Access Events Dataset Events Timeline Seasonal Calendar ACAPS Risk List Protection
  Monitoring Dataset* this product is not yet publicly available, but they will be
  published as standalone global products in the next weeks. ACAPS supports the earthquake
  response with a comprehensive data repository, providing both baseline pre-earthquake
  data, and in-crisis data. All these datasets are available with more frequent releases
  on the ACAPS API Please refer to http://www.acaps.org for the detailed codebooks
  of each dataset. For any inquiry please reach out to info@acaps.org. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package]'
details: 'Glide: EQ-2023-000015-TUR'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "This dataset aggregates secondary data from multiple ACAPS products\
    \ and the INFORM Severity Index as of 10 February 2023, capturing humanitarian\
    \ impact, access constraints, and protection monitoring outcomes from the February\
    \ 2023 T\xFCrkiye-Syria earthquake. The compilation integrates observational humanitarian\
    \ access events, severity assessments, and protection monitoring to provide a\
    \ multi-dimensional view of earthquake impacts on affected populations."
  sources:
  - id: source_1
    license: null
    name: INFORM Severity Index
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: ACAPS Humanitarian Access
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Humanitarian Access Events Dataset
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Protection Monitoring Dataset
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/acaps-turkiye-syria-earthquake-data-package
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Population affected by the 2023 T\xFCrkiye-Syria earthquake"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: ACAPS Turkiye-Syria Earthquake Data Package (Excel)
  download_url: https://data.humdata.org/dataset/d5afd76f-6d68-4117-9ef7-078c35ca4b8f/resource/6f0d829e-bf78-449b-886f-c7da98ad0016/download/20230210_acaps_turkiye_syria_data_package.xlsx
  format: null
  id: resource_6f0d829e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230210_ACAPS_Turkiye_Syria_Data_Package.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syrtur_acaps_earthquakedatapackage_20220301
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-03-01'
temporal_resolution: null
title: ACAPS Turkiye-Syria Earthquake Data Package
version: null
vulnerability: null
---
