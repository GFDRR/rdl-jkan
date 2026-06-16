---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) DTM
    url: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-idai-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-idai-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-idai-iom-dtm
dataset_id: rdls_lss-moz_iom_displacementdatabaselinea_2019
description: "Tropical cyclone Idai, on March 15th 2019, brought torrential rains\
  \ and winds affecting mostly the provinces of Manica, Sofala and Zamb\xE9zia, In\
  \ Mozambique, causing flash flooding and subsequent destruction. This dataset contains\
  \ DTM assessments containing number of affected people, their needs, geographic\
  \ locations etc.. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-idai-iom-dtm]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "IOM DTM conducted multi-round baseline assessments (Rounds 1, 2, 5,\
    \ and 6) following tropical cyclone Idai in March 2019 to document displacement,\
    \ affected populations, and humanitarian needs across Manica, Sofala, and Zamb\xE9\
    zia provinces. Data was collected through standard DTM methodology to track internally\
    \ displaced persons and returnees affected by cyclone-induced flooding and wind\
    \ damage."
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) DTM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-idai-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone Idai including displacement
      and needs assessment
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
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flash flooding triggered by cyclone Idai
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Of the 46 resettlement neighborhoods evaluated, most of the neighborhoods
    with (96%) are located in the Provinces. Sofala, Manica, and Zambezia, with 46,710
    people corresponding to 10,831 families; The displaced population remaining in
    accommodation centers and resettlement neighborhoods is estimated around 54,000
    people corresponding to 12,000 families.
  download_url: https://data.humdata.org/dataset/289a451a-8d6a-4211-bfbd-5f7f6afb2897/resource/adff7da9-3486-40af-849a-c5119b8e0bfd/download/dtm-mozambique-baseline-assessment-round-6.xlsx
  format: null
  id: resource_adff7da9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 6
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: An estimated 1,261 households and 7,730 individuals left their assessed
    locality to another district; More than 2,000,000 people whose homes were affected
    by shelter damage have stayed inside their locality; In Sofala and Zambezia reported
    a displaced population who have not returned to their locality of origin estimated
    at around 17,000 individuals and 4,000 households; The number of returned population
    who have returned to their locality of origin represents nearly 10,000 people
    and around 2,000 households.
  download_url: https://data.humdata.org/dataset/289a451a-8d6a-4211-bfbd-5f7f6afb2897/resource/440afc35-c16b-4a44-8cf9-d8b00183098e/download/dtm-mozambique-baseline-assessment-round-5.xlsx
  format: null
  id: resource_440afc35
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: From 27 May to 3 June, in close coordination with Mozambique's INGC,
    IOM DTM teams conducted baseline assessments at locality level. The assessment
    covered 19 districts in Sofala, Manica, Tete and Zambezia provinces. There are
    334+ K households and more than 1.5M affected individuals.
  download_url: https://data.humdata.org/dataset/289a451a-8d6a-4211-bfbd-5f7f6afb2897/resource/54db2f8f-2d18-4312-b39e-271b08b11066/download/dtm-mozambique-baseline-assessment-round-2.xlsx
  format: null
  id: resource_54db2f8f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Displacement Data - Baseline Assessment - Idai - [IOM DTM]
    (DTM Mozambique Baseline Assessment Round 1)
  download_url: https://data.humdata.org/dataset/289a451a-8d6a-4211-bfbd-5f7f6afb2897/resource/e18a7153-405a-4487-80b2-97e370e46816/download/dtm-mozambique-baseline-assessment-round-1.xlsx
  format: null
  id: resource_e18a7153
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_iom_displacementdatabaselinea_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-11-09'
  start: '2019-10-02'
temporal_resolution: null
title: Mozambique Displacement Data - Baseline Assessment - Idai - [IOM DTM]
version: null
vulnerability: null
---
