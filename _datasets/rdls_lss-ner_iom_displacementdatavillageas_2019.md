---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/niger-displacement-data-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/niger-displacement-data-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/niger-displacement-data-baseline-assessment-iom-dtm
dataset_id: rdls_lss-ner_iom_displacementdatavillageas_2019
description: 'This datasets has IDPs, Household & Returnees data at Admin3 level gathered
  through DTM Mobility Tracking Assessment.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/niger-displacement-data-baseline-assessment-iom-dtm]'
details: Round 8 is the latest Assessment as of July 2024.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM DTM conducted repeated Village Assessment Surveys (Rounds 1-9)
    across Niger using standardized key informant interviews and household questionnaires
    to enumerate internally displaced persons (IDPs), returnees (RAPDI), and affected
    households at commune level. Data were collected through structured surveys capturing
    demographic composition by age and sex, displacement origins, reasons for displacement,
    and current site characteristics, aggregated to Admin3 administrative divisions.
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
- href: https://data.humdata.org/dataset/niger-displacement-data-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees enumerated by household
      and individual counts across displacement sites
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
  description: The data collection for Round 9 was conducted from 25 November to 26
    December 2024. During this period, a total of 249,194 internally displaced persons
    (IDPs) were identified, along with 103,819 returnees. The Diffa region hosted
    the highest number of displaced individuals, with 174,208 IDPs and 88,820 returnees.
    It was followed by Tahoua, with 52,898 IDPs and 10,245 returnees, and Maradi,
    which recorded 22,088 IDPs and 4,754 returnees.
  download_url: https://data.humdata.org/dataset/0d776a1c-e2c0-49fc-857e-949be7013f99/resource/336ad1b1-0d0f-4f2c-8352-dedfaef74deb/download/dtm_niger_mt_village_assessment_survey_nov_2024.xlsx
  format: null
  id: resource_336ad1b1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Niger - Village Assessment - Round 9
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Displacement Data - Village Assessment Survey (VAS) [IOM DTM]
    (426, 988 IDP individuals and 84, 008 IDP households were identified in Round
    8.)
  download_url: https://data.humdata.org/dataset/0d776a1c-e2c0-49fc-857e-949be7013f99/resource/a574d503-2b94-4478-83bc-08b87b9fbbc7/download/vas_ki_r8_juillet_2024_final-dataset_publish_hdx.xlsx
  format: null
  id: resource_a574d503
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Niger - Village Assessment - Round 8
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In Round 7, 378 868 IDP individuals and 74 358 IDP households, 163
    611 returnees and 24 429 returnee households were identified.
  download_url: https://data.humdata.org/dataset/0d776a1c-e2c0-49fc-857e-949be7013f99/resource/aaa9b56f-5ef3-4e9a-9ce3-35128be5e4c6/download/donnees-vas_r7_public_hdx.xlsx
  format: null
  id: resource_aaa9b56f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Niger - Village Assessment - Round 7
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "This assessment provides information on the causes and periods of\
    \ displacement, the number of households and displaced persons and sectoral humanitarian\
    \ needs. Data collection was conducted from March 7 to April 9, 2023 in Diffa,\
    \ Maradi, Tillab\u221A\xA9ri and Tahoua regions. 353083 IDPs, 71251 IDP households,\
    \ and 66888 internal returnees were identified."
  download_url: https://data.humdata.org/dataset/0d776a1c-e2c0-49fc-857e-949be7013f99/resource/99389c48-79d5-41cf-9adb-189751b01422/download/niger-vas-round-6-dataset_website_hdx.xlsx
  format: null
  id: resource_99389c48
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Niger - Village Assessment - Round 6
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Displacement Data - Village Assessment Survey (VAS) [IOM DTM]
    (DTM Niger - Village Assessment - Round 5)
  download_url: https://data.humdata.org/dataset/0d776a1c-e2c0-49fc-857e-949be7013f99/resource/9f517825-4588-444d-81a3-b046cff3707e/download/dtm_niger_vas_round_5_septembre_2022_final.xlsx
  format: null
  id: resource_9f517825
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Niger - Village Assessment - Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Displacement Data - Village Assessment Survey (VAS) [IOM DTM]
    (DTM Niger - Village Assessment - Round 4)
  download_url: https://data.humdata.org/dataset/0d776a1c-e2c0-49fc-857e-949be7013f99/resource/a90f071a-e725-488f-89d9-86055c531ba2/download/vas_b3f_round-4_dataset_hdx.xlsx
  format: null
  id: resource_a90f071a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Niger - Village Assessment - Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Displacement Data - Village Assessment Survey (VAS) [IOM DTM]
    (DTM Niger - Village Assessment - Round 1)
  download_url: https://data.humdata.org/dataset/0d776a1c-e2c0-49fc-857e-949be7013f99/resource/84efcd03-2252-4b3a-a1f1-14fcb36820a2/download/hdx_dtm_niger_baseline_assessment_dec_2019_round_1.xlsx
  format: null
  id: resource_84efcd03
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Niger - Village Assessment - Round 1
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_iom_displacementdatavillageas_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-26'
  start: '2019-12-04'
temporal_resolution: null
title: Niger Displacement Data - Village Assessment Survey (VAS) [IOM DTM]
version: null
vulnerability: null
---
