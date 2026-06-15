---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/somalia-displacement-idps-returnees-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-displacement-idps-returnees-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-displacement-idps-returnees-baseline-assessment-iom-dtm
dataset_id: rdls_el-som_iom_displacementidpsreturnees_2020
description: 'The dataset contains IDPs, Returnees and host community at sub-national
  level.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-displacement-idps-returnees-baseline-assessment-iom-dtm]'
details: Round 3 is the latest Assessment as of September 2024.
exposure:
- asset_type:
    description: Internally displaced persons (IDPs), returnees, and host community
      populations at sub-national level
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
  description: IOM DTM conducted multi-round baseline assessments (Rounds 0-3, 2024)
    using standardized key informant interview methodology across Somali settlements
    to enumerate IDPs, returnees, and host community populations by demographic characteristics
    (age, sex) at sub-national administrative levels. Data aggregated from settlement-level
    surveys into regional and district-level population estimates.
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
- href: https://data.humdata.org/dataset/somalia-displacement-idps-returnees-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict and displacement events
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Returnee populations and affected host communities
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: DTM Somalia has mapped around 3,262,080 IDPs, 96,277 returnees, and
    9,455,907 residents in 12,090 assessed locations. IDPs were present in 42 percent
    of locations assessed (5,038 locations) and returnees were present in 3 percent
    of assessed locations (405 locations). Conflict and Natural Disaster (human-enhanced)
    are the primary reasons for displacement, each accounting for 41 percent.
  download_url: https://data.humdata.org/dataset/b421e1e5-a8cc-48c1-8e85-dc2d01706584/resource/343967e0-533d-4af2-aefe-85ff949061a9/download/somalia-baseline-assessment-dataset_-round-3-february-september-2024_hdx.xlsx
  format: null
  id: resource_343967e0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia - Baseline Assessment Dataset - Round 3 (February 2024 - September
    2024)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'In February and March 2023, IOM DTM implemented its second round of
    Baseline 2 exercise in three states of Somalia: Jubaland, Hirshabelle, and South
    West States. Baseline 2, an area based assessment, is the second step of Mobility
    Tracking implemented at settlement level and aims to quantify presence of population
    categories. This dataset covers 5,534 settlements (villages, neighborhoods or
    IDP sites) and records around 4,2 million residents, 1,2 million IDPs and 122,000
    returnees. The results include demographic, accessibility and reasons for displacement
    information, as well as the Operational Zones (OPZ) established by OCHA. These
    zones are designed to support sub-district response and reporting efforts.'
  download_url: https://data.humdata.org/dataset/b421e1e5-a8cc-48c1-8e85-dc2d01706584/resource/86f92eb8-504e-4685-bcc6-85121153c60e/download/dtm_som_baseline_assessment_r2_sws_jl_hs_2023_0-1.xlsx
  format: null
  id: resource_86f92eb8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia - Baseline Assessment Dataset - Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Between February 2020 and January 2022, IOM DTM implemented its first
    round of Baseline 2 exercise in Somalia. Baseline 2, an area-based assessment,
    is the second step of Mobility Tracking implemented at settlement level and aims
    to quantify presence of population categories. This Baseline 2 round 1 covered
    9,517 settlements in 17 regions. These settlements correspond to 6,029 villages,
    467 neighbourhoods, 432 rural IDP sites, and 2,589 urban IDP sites. Among the
    total of 4,574,256 IDPs reported, 3,664,282 reside in IDP sites and 909,974 live
    in the host communities. Regarding the returnee's population, 223,514 were returnees
    from abroad and 731,900 were previous IDPs (returnees from internal displacement).
  download_url: https://data.humdata.org/dataset/b421e1e5-a8cc-48c1-8e85-dc2d01706584/resource/6e3fc251-1dfc-435c-8652-5e1ad198119d/download/iom_dtm_somalia_baseline2_round1_31012022_hdx.xlsx
  format: null
  id: resource_6e3fc251
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia - Baseline Assessment Dataset - Round 1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Displacement - [IDPs, Returnees] - Baseline Assessment [IOM
    DTM] (Somalia - Baseline Assessment Dataset - Round 0)
  download_url: https://data.humdata.org/dataset/b421e1e5-a8cc-48c1-8e85-dc2d01706584/resource/bc837fb4-0390-411c-91eb-01bafe4e8052/download/mobility-tracking-b2-public-use.xlsx
  format: null
  id: resource_bc837fb4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia - Baseline Assessment Dataset - Round 0
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_iom_displacementidpsreturnees_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-09-19'
  start: '2020-02-01'
temporal_resolution: null
title: Somalia Displacement - [IDPs, Returnees] - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
