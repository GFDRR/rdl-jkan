---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-northern-mozambique-crisis-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-northern-mozambique-crisis-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-northern-mozambique-crisis-iom-dtm
dataset_id: rdls_lss-moz_iom_displacementdatabaselinea_2022
description: 'The increase of security incidents in northern Mozambique since 2017
  resulted in population displacement as well as subsequent humanitarian needs in
  virtually every humanitarian sector. To better understand the scope of displacement
  and needs of displaced populations, and in light of the intensification of the situation,
  the International Organization for Migration (IOM) activated its Displacement Tracking
  Matrix (DTM) in the Cabo Delgado province in February 2019.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-northern-mozambique-crisis-iom-dtm]'
details: Round 22 is the latest Assessment as of April 2025.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM activated displacement tracking in Cabo Delgado province in
    February 2019 in response to escalating security incidents since 2017. Data collected
    through repeated baseline assessment rounds (12-22) from February 2019 to April
    2025 across multiple provinces, capturing IDP demographics, displacement triggers
    (conflict, climate disasters, health hazards), and humanitarian needs through
    standardized survey methodology.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-displacement-data-baseline-assessment-northern-mozambique-crisis-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from armed conflict and insecurity in
      northern Mozambique
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
  - asset_category: population
    asset_dimension: population
    description: Population displacement due to climate disasters including drought,
      flood, and cyclones
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
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This report presents key findings from Mobility Tracking Round 22,
    conducted across Central, Northern, and Southern Mozambique between February and
    March 2025. Data was collected through key informant interviews and group discussions
    at locality and site levels. The Mobility Tracking exercise provides a comprehensive
    geographic overview of the demographic and mobility dynamics of internally displaced
    persons (IDPs) and returnees across Mozambique, informing evidence-based humanitarian
    and durable solutions planning. During this round, IOM's Displacement Tracking
    Matrix (DTM) identified a total of 609,243 IDPs and 701,462 returnees across 400
    assessed locations.
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/c3cf5028-cb98-4d1c-adf1-52f78927b805/download/mozambique-crisis-mt-round-22-april-2025.xlsx
  format: null
  id: resource_c3cf5028
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mozambique Crisis -MT Round 22 (April 2025).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset presents findings of Mobility Tracking Assessments round
    21 (previously known as Baseline Assessments) conducted across Central and Southern
    Mozambique through key-informant and group interviews at location level between
    May and June 2024. Mobility Tracking assessments provides a geographical overview
    of demographic and mobility profiles of internally displaced persons (IDPs) and
    returnees across Mozambique. During this round, IOM DTM mapped a total of 28,116
    households hosting 139,333 IDPs in 107 locations. Ninety eight per cent of the
    IDPs were identified in 93 displacement sites whilst two per cent are living in
    host communities. The period of displacement being considered spans from 2017
    to 2024 and 99 per cent of the displacements were due to climatic conditions.
    Sofala hosts 64 per cent of the overall IDP figure followed by Manica (20%). Comparing
    to the previous round, there is a 10 per cent increase in the number of IDPs in
    Central attributable to widened coverage and recent drought related displacements
    in Manica province.
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/231f5128-4a20-4565-80d2-67e79416d033/download/dtm_moz_mobility_tracking_assessment_r21_final_public-dataset_july-2024_hdx.xlsx
  format: null
  id: resource_231f5128
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mozambique Crisis - MT Round 21 (Jun 2024).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset is the 20th round of Mobility Tracking Assessments conducted
    across Mozambique through key-informant assessments and group interviews at the
    location level in December 2023. Mobility Tracking assessments estimate the presence
    of internally displaced persons (IDPs) and returnees across Mozambique. IOM DTM
    mapped a total of 709,529 IDPs and 632.408 returnees in round 20.
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/a6f9f9b8-d265-4099-9ead-5e65fd26c074/download/dtm_moz_mobility_tracking_assessment_r20_public-dataset_hdx.xlsx
  format: null
  id: resource_a6f9f9b8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mozambique Crisis - MT Round 20 (Dec 2023).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This summary presents findings of the 19th round of Mobility Tracking
    Assessments (previously known as Baseline Assessments) conducted across Northern
    and Central Mozambique through key-informant assessments and group interviews
    at location level between July and August 2023. Mobility Tracking assessments
    estimate the presence of internally displaced persons (IDPs) and returnees across
    Mozambique. IOM DTM mapped a total of 850,599 IDPs and 571,468 returnees in 325
    locations. Overall increase on the number of IDPs and Returnees is attributable
    to the widened coverage. Comparing with previous assessments which covered only
    Northern Mozambique, the July-August 2023 assessment was widened to cover Manica,
    Sofala, Tete and Zambezia provinces.
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/6a2b6c5f-5cac-4ca7-b547-8198a56ee2d8/download/hdx_northern-mozambique-crisis-mt-round-19-sep-2023.xlsx
  format: null
  id: resource_6a2b6c5f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Northern and Central Mozambique Crisis - MT Round 19 (Sep 2023).xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This summary presents findings of the 18th round of Mobility Tracking
    Assessments (previously known as Baseline Assessments) conducted across Northern
    Mozambique through key-informant assessments and group interviews at district
    and location-level in March 2023. Mobility Tracking assessments estimate the presence
    of internally displaced persons (IDPs) and returnees across Northern Mozambique.
    IOM DTM mapped a total of 834,304 IDPs and 420,200 returnees in 221 locations.
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/6382112b-7093-47b1-b9f4-fc29e09f067c/download/hdx_northern_mozambique_round_18.xlsx
  format: null
  id: resource_6382112b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 18
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Increased security incidents in northern Mozambique since 2017 resulted
    in population displacement as well as subsequent humanitarian needs. To better
    understand the scope of displacement trends and needs of displaced populations,
    the International Organization for Migration (IOM) activated DTM in Cabo Delgado
    province in February 2019. In the 16th round of Baseline Assessments, key-informant
    interviews were conducted at district and location-level between May and June
    2022. Assessments estimate the presence of 946,508 internally displaced persons
    (IDPs) mapped across displacement sites and host communities in 212 localities.
    Security and access restraints in the districts of Nangade, Macomia, Meluco, Mocimboa
    da Praia, Quissanga, Muidumbe and Palma, have limited data collection to select
    localities accessible to DTM field teams and focal points. For this round, 30%
    of 946,508 IDPs are mapped in relocation sites, temporary centers and host community
    extensions. Approximately 1% of total IDPs present at the time of assessment were
    mapped in Pemba (139,566 individuals), followed by Metuge (126,030 individuals),
    Nangade (116,538 individuals), Mueda (104,270 individuals) and Ancuabe (82,496
    individuals).
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/ae1e1c3a-48b9-4a49-81de-1344149f2018/download/northern-mozambique-crisis-baseline-assessment-dataset-round-16-june-2022.xlsx
  format: null
  id: resource_ae1e1c3a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 16
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: For R15 baseline assessment, key-informant interview were conducted
    at district and location-level between January and February 2022. Assessments
    estimate the presence of 784,564 internally displaced persons (IDPs) mapped across
    displacement sites and host communities in 208 localities. Security and access
    restraints in the districts of Nangade, Macomia, Meluco, Mocimboa da Praia, Quissanga,
    Muidumbe and Palma, have limited data collection to select localities accessible
    to DTM held teams and focal points. For this round, 28% of 784,564 IDPs are mapped
    in relocation sites, temporary centers and host community extensions. One-fitth
    of total IDPs present at the time of assessment were mapped in Pemba (151,987
    individuals), followed by Metuge (124,036 individuals), Mueda (84,822 individuals),
    Ancuabe (72,526 individuals) and Nangade (64,866 individuals).
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/eb1a680c-fa9b-47c2-a77a-7c02bb23b579/download/hdx-northern-mozambique-crisis-baseline-assessment-dataset-round-15-public-dataset_1.xlsx
  format: null
  id: resource_eb1a680c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 15
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Displacement Data - Baseline Assessment - Northern Mozambique
    Crisis - [IOM DTM] (DTM Mozambique Baseline Assessment Round 14)
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/ca292243-5aff-4599-a371-a1452e711178/download/northern-mozambique-crisis-baseline-assessment-dataset-round-14-public-dataset.xlsx
  format: null
  id: resource_ca292243
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 14
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Displacement Data - Baseline Assessment - Northern Mozambique
    Crisis - [IOM DTM] (DTM Mozambique Baseline Assessment Round 13)
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/60128696-35ae-4ce9-8c65-c1906d7c917c/download/hdx-northern-mozambique-crisis-baseline-assessment-dataset-round-13-plubic-dataset.xlsx
  format: null
  id: resource_60128696
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 13
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The twelfth round of the DTM Baseline assessment was carried out in
    155 localities, located in the provinces of Cabo Delgado (102 localities), Nampula
    (36 localities), Niassa (9 localities), Sofala (2 localities) and Zambezia (6
    localities). As of April 2021, an estimated 662,828 IDPs were identied in Cabo
    Delgado, while an additional 66,913 IDPs were identied in Nampula, 1,200 in Zambezia,
    1,133 in Niassa, and 153 in Sofala. This brings the total number of individuals
    displaced in the five provinces to 732,227* Internally Displaced Persons, or 155,494
    displaced families. Overall, 23% of the IDP population is male, 31% female, and
    46% are children.
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/fb30fe2a-f46c-42c9-afb7-f244c37980fb/download/hdx_northern-mozambique-crisis-baseline-assessment-dataset-round-12.xlsx
  format: null
  id: resource_fb30fe2a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Mozambique Baseline Assessment Round 12
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset presents findings of Mobility Tracking Assessments round
    21 (previously known as Baseline Assessments) conducted across Central and Southern
    Mozambique through key-informant and group interviews at location level between
    May and June 2024. Mobility Tracking assessments provides a geographical overview
    of demographic and mobility profiles of internally displaced persons (IDPs) and
    returnees across Mozambique. During this round, IOM DTM mapped a total of 28,116
    households hosting 139,333 IDPs in 107 locations. Ninety eight per cent of the
    IDPs were identified in 93 displacement sites whilst two per cent are living in
    host communities. The period of displacement being considered spans from 2017
    to 2024 and 99 per cent of the displacements were due to climatic conditions.
    Sofala hosts 64 per cent of the overall IDP figure followed by Manica (20%). Comparing
    to the previous round, there is a 10 per cent increase in the number of IDPs in
    Central attributable to widened coverage and recent drought related displacements
    in Manica province.
  download_url: https://data.humdata.org/dataset/a4bbccf1-d5ae-4712-b378-29c1372c7a42/resource/9eaa4561-f061-40aa-9e6f-dd5ca95484fc/download/dtm_moz_mobility_tracking_assessment_r21_final_public-dataset_july-2024_hdx.xlsx
  format: null
  id: resource_9eaa4561
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mozambique Crisis - MT Round 21 (Jun 2024).xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_iom_displacementdatabaselinea_2022
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
  end: '2025-03-31'
  start: '2022-02-01'
temporal_resolution: null
title: Mozambique Displacement Data - Baseline Assessment - Northern Mozambique Crisis
  - [IOM DTM]
version: null
vulnerability: null
---
