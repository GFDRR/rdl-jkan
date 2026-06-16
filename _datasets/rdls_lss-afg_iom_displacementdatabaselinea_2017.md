---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/afghanistan-displacement-data-baseline-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/afghanistan-displacement-data-baseline-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/afghanistan-displacement-data-baseline-assessment-iom-dtm
dataset_id: rdls_lss-afg_iom_displacementdatabaselinea_2017
description: 'The dataset contains IDPs, returnees at sub national level.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-displacement-data-baseline-assessment-iom-dtm]'
details: Please look at the [flow monitoring](https://data.humdata.org/dataset/afghanistan-flow-monitoring-counting-data-iom-dtm)
  data which maybe useful for understanding the situation.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted repeated baseline assessments across multiple rounds
    (1-16) using standardized methodology to track displacement populations (arrival
    IDPs, returnees from abroad, returned IDPs, outmigrants) at settlement and district
    administrative levels in Afghanistan. Data aggregated by province, district, and
    settlement with temporal tracking from 2011 onwards.
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
- href: https://data.humdata.org/dataset/afghanistan-displacement-data-baseline-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees from flood-related displacement
      in Afghanistan
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
  description: IOM Afghanistan launched the first round of the DTM Baseline Area Assessment
    B1 in January 2024 as part of its ongoing efforts to collect crucial data on population
    mobility dynamics, specifically displacement and returns. In particular, the B1
    activity seeks to map the presence of mobile population groups, such as Internally
    Displaced Persons (IDPs), returnees, and internal migrants, to enable further
    understanding of conditions, vulnerabilities, and humanitarian needs through targeted
    data collection and analysis.
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/9596a168-23af-4772-b081-d94faeab3329/download/b1-mobility-data-only-b1_publish.xlsx
  format: null
  id: resource_9596a168
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Round 1 Baseline Assessment B1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM identified an estimated 6,557,000 individuals who have displaced
    since 2012 and remain in displacement, marking an 11% increase since Round 15
    (March and April 2022). Individuals who have returned from displacement since
    2012 reached approximately 11,036,000, which marks a 10% increase since the previous
    round. DTM identified around 6,842,800 individuals who have crossed international
    borders since 2012 and remain abroad. This is a 21% increase. Finally, cross-border
    returnees since 2012 amount to around approximately 6,545,900, which is a 14%
    increase compared to Round 15.
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/b9e438e0-b68a-49f9-b9a9-68c0f3e93603/download/dtm-afghanistan-baseline-assessment-settlement_round_16_hdx.xlsx
  format: null
  id: resource_b9e438e0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 16 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Settlements Round 15 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/62ad6e55-5f5d-4494-854c-4110687e9e2b/download/hdx_afghanistan-baseline-assessment-settlement-round15.xlsx
  format: null
  id: resource_62ad6e55
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 15 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Districts Round 15 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/c3f001fa-b45b-464c-9460-1ca79fd39b49/download/hdx_afghanistan-baseline-assessment-district-round15.xlsx
  format: null
  id: resource_c3f001fa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 15 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In Afghanistan, DTM employs the Baseline Mobility Assessment tool,
    designed to track mobility, determine the population sizes, locations and geographic
    distribution of forcibly displaced, return and migrant populations, reasons for
    displacement, places of origin, and times of displacement, as well as basic demographics,
    vulnerabilities and priority needs. Data is collected at the settlement level,
    through community focus group discussions with key informants and direct observations.
    As of 31 December 2021, 34 provinces, 401 districts and 13,187 settlements have
    been assessed, including interviews with 82,923 community focal points. Between
    2012 and December 2021, 5,149,245 returned migrants from abroad and 5,832,454
    arrival IDPs currently living in host communities were identified
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/7cf3cec8-dbbc-4c96-9762-1464cd0bff75/download/hdx_afg_baseline-assessment-settlement-round-14.xlsx
  format: null
  id: resource_7cf3cec8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 14 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Districts Round 14 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/1e7d4907-f66e-4cf8-8b48-fa8b599a3487/download/hdx_afg_baseline_assessment_district_round-14.xlsx
  format: null
  id: resource_1e7d4907
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 14 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Settlements Round 13 Baseline Assessment-30-2021.xlsx)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/8310fd03-3b1b-41b3-be53-3b4dc5a2b4a1/download/hdx_dtm_afghanistan_baseline_aassessment_ssettlement_round_13_jun-30-2021.xlsx
  format: null
  id: resource_8310fd03
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 13 Baseline Assessment-30-2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Districts Round 13 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/0e2469f4-e636-4bfd-b857-64365bc031da/download/hdx_afghanistan-baseline-assessment-district-round-13_jun-30-2021.xlsx
  format: null
  id: resource_0e2469f4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 13 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: In Afghanistan, DTM employs the Baseline Mobility Assessment tool,
    designed to track mobility, determine the population sizes, locations and geographic
    distribution of forcibly displaced, return and migrant populations, reasons for
    displacement, places of origin, and times of displacement, as well as basic demographics,
    vulnerabilities and priority needs. Data is collected at the settlement level,
    through community focus group discussions with key informants and direct observations.
    As of 34 March 2021, 34 provinces, 401 districts and 12,882 settlements have been
    assessed, including interviews with 77,019 key informants. Between 2012 and March
    2021, 4,359,961 returnees from abroad, 6,514,365 internal returnees and 4,927,639
    IDPs currently living in host communities were identified.
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/94e2e1f6-6498-4091-b0a8-1ede402ffc2f/download/hdx_afghanistan-baseline-assessment-settlement-round-12_mar-31-2021.xlsx
  format: null
  id: resource_94e2e1f6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 12 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Districts Round 12 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/a0a902e1-b19e-490b-b186-75d2d17d5104/download/hdx_afghanistan-baseline-assessment-district-round-12_mar-31-2021_0.xlsx
  format: null
  id: resource_a0a902e1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 12 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Settlements Round 11 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/60940c1e-a83b-4218-a8ea-e0f3f069ce18/download/dtm-afghanistan-settlements-round-11-baseline-assessment.xlsx
  format: null
  id: resource_60940c1e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 11 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Districts Round 11 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/d3a63782-774e-4cbb-abd0-952be09fb946/download/dtm-afghanistan-districts-round-11-baseline-assessment.xlsx
  format: null
  id: resource_d3a63782
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 11 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: As of 30 June 2020, 34 provinces, 397 districts and 12,335 settlements
    have been assessed, including interviews with 62,194 key informants. Between 2012
    and June 2020, 3,881,903 returnees and 4,760,478 IDPs currently living in host
    communities were identified.
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/91598e80-0293-4652-a5ed-552ca316361e/download/dtm-afghanistan-settlements-round-10-baseline-assessment.xlsx
  format: null
  id: resource_91598e80
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 10 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: As of 30 June 2020, 34 provinces, 397 districts and 12,335 settlements
    have been assessed, including interviews with 62,194 key informants. Between 2012
    and June 2020, 3,881,903 returnees and 4,760,478 IDPs currently living in host
    communities were identified.
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/3b286f87-b0e6-485a-aba2-07609e137ea0/download/dtm-afghanistan-districts-round-10-baseline-assessment.xlsx
  format: null
  id: resource_3b286f87
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 10 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 34 provinces covered. 392 districts assessed (7 districts were inaccessible
    & 2 districts had no presence of IDPs or returnees). 11,671 settlements assessed.
    62,214 key informants interviewed. 3,451,510 returnees from abroad [2012-2019].
    4,350,900 IDPs [2012-2019] currently in host communities. 4,753,717 former IDPs
    have returned to their homes [2012-2019]. 2,531,011 out-migrants fled abroad [2012-2019]
    332,253 out-migrants fled to Europe (13% of out-migrants) 460,733 returnees and
    IDPs (6%) live in tents or in the open air.
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/fe52a729-8c4c-494d-9dfc-4531bff24439/download/dtm-afghanistan-settlements-round-9-baseline-assessment.xlsx
  format: null
  id: resource_fe52a729
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 9 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Districts Round 9 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/1f133dff-de9b-41f1-ae93-ad68ef7b2b95/download/dtm-afghanistan-districts-round-9-baseline-assessment.xlsx
  format: null
  id: resource_1f133dff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 9 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: As of 30 June 2019, 34 provinces, 392 districts and 11,636 settlements
    have been assessed, including interviews with 61,748 key informants. Between 2012
    and June 2019, 3,309,188 returnees and 4,191,521 IDPs currently living in host
    communities were identified.
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/cd02d289-3cf1-4bba-a638-9cacb76bf7ee/download/dtm-afghanistan-settlements-round-8-baseline-assessment.xlsx
  format: null
  id: resource_cd02d289
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 8 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (DTM
    Afghanistan Districts Round 8 Baseline Assessment)
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/56ad59ca-5115-48de-997b-5ef8ebcd0c7c/download/dtm-afghanistan-districts-round-8-baseline-assessment.xlsx
  format: null
  id: resource_56ad59ca
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 8 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-7: The dataset has IDPs, returnees and refugees at sub national
    level along with lat/lon coordinates. The dataset also has settlement types of
    the returnees.'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/6ba655ff-e886-4d4d-89c9-5784c224b500/download/dtm-afghanistan-settlements-round-7-baseline-assessment.xlsx
  format: null
  id: resource_6ba655ff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 7 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-7: The dataset contains IDPs and documented & undocumented Returnees
    from Pakistan,Iran and other countries per district and breakdown by year 2012_2015,
    2016, 2017 and 2018'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/dd0554a2-2c21-475b-9cce-77eb67f65139/download/dtm-afghanistan-districts-round-7-baseline-assessment.xlsx
  format: null
  id: resource_dd0554a2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 7 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-6: The dataset has IDPs, returnees and refugees at sub national
    level along with lat/lon coordinates. The dataset also has settlement types of
    the returnees.'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/b0ebf6bb-bd68-4a6a-8f26-26cf6b4a60e4/download/dtm-afghanistan-settlements-round-6-baseline-assessment.xlsx
  format: null
  id: resource_b0ebf6bb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 6 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-6: The dataset contains IDPs and documented & undocumented Returnees
    from Pakistan,Iran and other countries per district and breakdown by year 2012_2015,
    2016, 2017 and 2018'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/e61781eb-3303-4729-af37-66e55af88597/download/dtm-afghanistan-districts-round-6-baseline-assessment.xlsx
  format: null
  id: resource_e61781eb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 6 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (Round-5:
    The dataset contains IDPs, returnees and refugees at sub national level)'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/f06a1277-f46e-4eca-b8c6-dde4618a645b/download/dtm-afghanistan-settlements-round-5-baseline-assessment.xlsx
  format: null
  id: resource_f06a1277
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 5 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-5: The dataset contains IDPs and documented & undocumented Returnees
    from Pakistan,Iran and other countries per district and breakdown by year'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/604041a0-b86a-4b31-8ac5-f61c13c86753/download/dtm-afghanistan-districts-round-5-baseline-assessment.xlsx
  format: null
  id: resource_604041a0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 5 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (Round-4:
    The dataset contains IDPs, returnees and refugees at sub national level)'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/fc72cbf1-7615-4f11-bb95-580b969d544d/download/dtm-afghanistan-settlements-round-4-baseline-assessment.xlsx
  format: null
  id: resource_fc72cbf1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 4 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-4: The dataset contains IDPs and documented & undocumented Returnees
    from Pakistan,Iran and other countries per district and breakdown by year'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/02ddc996-8dc3-4af9-b85b-f959b051ee54/download/dtm-afghanistan-districts-round-4-baseline-assessment.xlsx
  format: null
  id: resource_02ddc996
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 4 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (Round-3:
    The dataset contains IDPs, returnees and refugees at sub national level)'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/43f94f00-0b9f-4839-9174-b5875def7600/download/dtm-afghanistan-settlements-round-3-baseline-assessment.xlsx
  format: null
  id: resource_43f94f00
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 3 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-3: The dataset contains IDPs and documented & undocumented Returnees
    from Pakistan,Iran and other countries per district and breakdown by year'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/61df60d0-64a9-4ee8-9730-2c68e0d58f6f/download/dtm-afghanistan-districts-round-3-baseline-assessment.xlsx
  format: null
  id: resource_61df60d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 3 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (Round-2:
    The dataset contains IDPs, returnees and refugees at sub national level)'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/39e64c24-c723-40aa-89c5-93dc1609f6c4/download/dtm-afghanistan-settlements-round-2-baseline-assessment.xlsx
  format: null
  id: resource_39e64c24
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 2 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Round-2: The dataset contains IDPs and documented & undocumented Returnees
    from Pakistan,Iran and other countries per district and breakdown by year'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/94335c32-b7de-4ffd-b660-fac4e83e6358/download/dtm-afghanistan-districts-round-2-baseline-assessment.xlsx
  format: null
  id: resource_94335c32
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Districts Round 2 Baseline Assessment
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan Displacement Data - Baseline Assessment [IOM DTM] (Round-1:
    The dataset contains IDPs, returnees and refugees at sub national level)'
  download_url: https://data.humdata.org/dataset/90deb235-1bf5-4bae-b231-3393222c2d00/resource/a920cde5-24e2-40c9-974c-959c2f46e7cc/download/dtm-afghanistan-settlements-round-1-baseline-assessment.xlsx
  format: null
  id: resource_a920cde5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Afghanistan Settlements Round 1 Baseline Assessment
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_iom_displacementdatabaselinea_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-02-29'
  start: '2017-02-01'
temporal_resolution: null
title: Afghanistan Displacement Data - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
