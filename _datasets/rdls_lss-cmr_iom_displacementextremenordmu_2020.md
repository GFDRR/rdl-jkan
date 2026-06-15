---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    url: https://data.humdata.org/dataset/cameroon-displacement-extreme-nord-msna-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/cameroon-displacement-extreme-nord-msna-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/cameroon-displacement-extreme-nord-msna-iom-dtm
dataset_id: rdls_lss-cmr_iom_displacementextremenordmu_2020
description: 'This dataset contains the results of a multisectoral assessment of the
  needs of displaced populations .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cameroon-displacement-extreme-nord-msna-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "IOM DTM conducted five rounds of multisectoral needs assessments (MSNA)\
    \ of internally displaced persons and returnees in Cameroon's Extr\xEAme-Nord\
    \ region. Data were collected through household surveys and compiled into structured\
    \ datasets documenting displacement impacts and sectoral needs across multiple\
    \ assessment cycles."
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cameroon-displacement-extreme-nord-msna-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Displacement of populations affected by conflict and insecurity\
      \ in Extr\xEAme-Nord region"
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
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Multisectoral needs assessment of affected and displaced populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: "This dataset thus provides an overview of the displacement situation\
    \ and the humanitarian needs of displaced populations. The data collection on\
    \ multisectoral needs was conducted between 23 August and 4 September 2024, covering\
    \ 7,220 households and a total of 47,051 individuals across the six departments\
    \ of the Far North region (Diamar\xE9, Logone-Et-Chari, Mayo-Danay, Mayo-Kani,\
    \ Mayo-Sava, and Mayo-Tsanaga). The questionnaire was developed by IOM, OCHA,\
    \ and the various humanitarian sectors. The overview of needs was obtained following\
    \ joint data analysis conducted with the lead agencies of each sector."
  download_url: https://data.humdata.org/dataset/688eca47-ef79-4a03-a21c-7e5d9ea0e8d9/resource/ec8e51d8-8e4c-42d3-83ec-093d3df31062/download/dtm_cameroun_msna_menage_aout_2024_round_5.xlsx
  format: null
  id: resource_ec8e51d8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CMR MNSA Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "The round 4 data collection was conducted between August 18 and August\
    \ 29, 2023, among 5,801 households in the six departments (Diamar\xE9, Logone-Et-Chari,\
    \ Mayo-Danay, Mayo-Kani, Mayo Sava, and Mayo-Tsanaga) of the Extreme North region.\
    \ This was done using a questionnaire developed by IOM, OCHA, and various sectors.\
    \ An overview of the needs was obtained following joint data analysis with the\
    \ lead representatives from each sector."
  download_url: https://data.humdata.org/dataset/688eca47-ef79-4a03-a21c-7e5d9ea0e8d9/resource/f6dc1732-ca6d-4186-bc88-8c7fed8b6315/download/iom_dtm_bdd_msna_hh_round-4.xlsx
  format: null
  id: resource_f6dc1732
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CMR MNSA Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A multi-sectoral needs assessment (MSNA) was conducted in Cameroon
    between August 11 and 24, 2022 in all departments of the Far North. This evaluation
    was conducted in 1,017 localities hosting the target populations in the six departments
    of the Far North, by a total of 132 enumerators, with 3,884 key trainers. The
    collection exercise was carried out with the assistance of OCHA, sectors active
    in the Far North and the local NGO COHEB in order to provide humanitarian partners
    with an overview of the priority sectoral needs of vulnerable populations, including
    among host populations, in localities hosting mobile populations (displaced, returned
    or refugees out of camp).
  download_url: https://data.humdata.org/dataset/688eca47-ef79-4a03-a21c-7e5d9ea0e8d9/resource/ff718655-a93f-493f-aeb7-29a7bce7cc6f/download/hdx_dtm_cameroon_msna_round_3_sept_2022.xlsx
  format: null
  id: resource_ff718655
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CMR MNSA Round 3
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A multi-sector needs assessment (MSNA) was conducted in Cameroon between
    July 7 and July 18 2021 in all the departments of the Far North. This assessment
    was carried out in 1,023 localities in the six departments of the Far North, by
    a total of 101 enumerators, with 2,795 key informants. The data collection exercise
    was carried out with the support of OCHA, sectors active in the Far North and
    the local NGO COHEB in order to provide humanitarian partners with an overview
    of the priority sectoral needs of vulnerable populations, including among host
    populations, in localities hosting mobile populations (displaced, returnees or
    refugees outside the camp).
  download_url: https://data.humdata.org/dataset/688eca47-ef79-4a03-a21c-7e5d9ea0e8d9/resource/4ddd679e-f817-4e61-9c5e-b58da00aad5f/download/hdx_dtm_cameroon_msna_round_2.xlsx
  format: null
  id: resource_4ddd679e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CMR MNSA Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset contains the results of a multisectoral assessment of
    the needs of vulnerable populations carried out in the Far North between November
    17 and December 7, 2020. This assessment was carried out in 888 localities in
    the six departments of the Far North, by a total of 102 enumerators, from 2,578
    key informants. The data collection exercise was carried out with the support
    of OCHA, sectors active in the Far North and two local NGOs in order to provide
    humanitarian partners with an overview of the priority sectoral needs of vulnerable
    populations, including among the host populations, in the localities hosting mobile
    populations (displaced, returnees or refugees outside the camp.
  download_url: https://data.humdata.org/dataset/688eca47-ef79-4a03-a21c-7e5d9ea0e8d9/resource/cbe44149-0bdc-4c55-b9b0-8fab7cdc59e8/download/dtm-cmr-mnsa-round-1.xlsx
  format: null
  id: resource_cbe44149
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM CMR MNSA Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cmr_iom_displacementextremenordmu_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-09-04'
  start: '2020-11-17'
temporal_resolution: null
title: "Cameroon Displacement - Extr\xEAme-Nord - Multi-Sectoral Needs Assessment\
  \ (MSNA) [IOM DTM]"
version: null
vulnerability: null
---
