---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Cadre Harmonis\xE9 (CH)"
    url: https://data.humdata.org/dataset/cadre-harmonise
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Integrated Food Security Phase Classification (IPC)
    url: https://data.humdata.org/dataset/cadre-harmonise
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CILSS
    url: https://data.humdata.org/dataset/cadre-harmonise
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Food Security and Nutrition Working Group, West and Central Africa
  url: https://data.humdata.org/dataset/cadre-harmonise
creator:
  affiliation: null
  email: null
  name: Food Security and Nutrition Working Group, West and Central Africa
  url: https://data.humdata.org/dataset/cadre-harmonise
dataset_id: rdls_lss-food_security_a_datacadreharmonisechinteg_2014
description: "The Cadre Harmonis\xE9 (CH) and Integrated Food Security Phase Classification\
  \ (IPC) are analytical frameworks which synthesize indicators of food and nutrition\
  \ security outcomes and the inference of contributing factors into scales and figures\
  \ representing the nature and severity of crisis and implications for strategic\
  \ response in food security and nutrition. There is also a global Acute Food Insecurity\
  \ Country dataset .. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cadre-harmonise]"
details: 'The Cadre Harmonise leads two cycle of analyses every year. One around October/November
  (after the publication of harvest forecasts and the results of nutrition and market
  surveys), and one around February/March (after the publication of the final results
  of agricultural production and any new data on nutrition, HEA, food consumption,
  etc.). The validity periods of the analyses are the same every year and they cover:
  March-May (current) and June-August (projection) for the March cycle, and October-December
  (current) and June-August (projection) for the November cycle of analysis. The latest
  data for Niger is not yet available.'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Food security and nutrition data from government sources, CILSS, and\
    \ IPC assessments are synthesized through the Cadre Harmonis\xE9 analytical framework,\
    \ which integrates indicators of food consumption, livelihoods, nutrition, and\
    \ mortality outcomes into standardized phase classifications (1-5) representing\
    \ crisis severity. The resulting dataset provides spatially-referenced food insecurity\
    \ phase classifications and affected population counts at multiple administrative\
    \ levels across West and Central Africa from 2014 onwards."
  sources:
  - id: source_1
    license: null
    name: "Cadre Harmonis\xE9 (CH)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Integrated Food Security Phase Classification (IPC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: CILSS
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cadre-harmonise
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity phase classification and affected population counts
      from drought and food security crisis
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
  url: https://www.cadreharmonise.org/en_GB
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://www.cadreharmonise.org/en_GB/documentation
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://github.com/idiise/CHdataimprovement/blob/master/README.md
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: West & Central Africa Food Security Data - Cadre Harmonise (CH) and
    Integrated Food Security Phase Classification (IPC) data (CH and IPC data)
  download_url: https://data.humdata.org/dataset/5123033a-2db1-496c-b381-df804ac30595/resource/c689cb9f-2475-4b7e-8beb-178ed9f6253d/download/cadre_harmonise_caf_ipc_dec25.xlsx
  format: null
  id: resource_c689cb9f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cadre_harmonise_caf_ipc_Dec25.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: West & Central Africa Food Security Data - Cadre Harmonise (CH) and
    Integrated Food Security Phase Classification (IPC) data (geo files of march 2023
    projected CH figures and indicators)
  download_url: https://data.humdata.org/dataset/5123033a-2db1-496c-b381-df804ac30595/resource/325a0aaa-0da9-4f8d-9ad4-3e16a6d231b2/download/wca_chipc_projected_march2023.geojson
  format: null
  id: resource_325a0aaa
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wca_CHIPC_projected_march2023.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: West & Central Africa Food Security Data - Cadre Harmonise (CH) and
    Integrated Food Security Phase Classification (IPC) data (geo files of march 2023
    current CH figures and indicator)
  download_url: https://data.humdata.org/dataset/5123033a-2db1-496c-b381-df804ac30595/resource/8eba40e7-e6aa-4887-a950-2568a1e76f8c/download/wca_chipc_current_march2023.geojson
  format: null
  id: resource_8eba40e7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wca_CHIPC_current_march2023.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: West & Central Africa Food Security Data - Cadre Harmonise (CH) and
    Integrated Food Security Phase Classification (IPC) data (documentation on CH
    data - english)
  download_url: https://data.humdata.org/dataset/5123033a-2db1-496c-b381-df804ac30595/resource/cf0b5c90-c281-4802-8ddd-e18a936cea06/download/consolidation-of-ch-data-2014-march-2023-en.pdf
  format: null
  id: resource_cf0b5c90
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Consolidation of CH data 2014 - March 2023 en.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "West & Central Africa Food Security Data - Cadre Harmonise (CH) and\
    \ Integrated Food Security Phase Classification (IPC) data (documentation sur\
    \ les donn\xE9es CH - fran\xE7ais)"
  download_url: https://data.humdata.org/dataset/5123033a-2db1-496c-b381-df804ac30595/resource/4401e1fd-1060-4d6e-82b3-c4bb6b200484/download/consolidation-de-donnees-ch-2014-mars-2023-fr.pdf
  format: null
  id: resource_4401e1fd
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Consolidation de Donnees CH 2014 - Mars 2023 fr.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: West & Central Africa Food Security Data - Cadre Harmonise (CH) and
    Integrated Food Security Phase Classification (IPC) data (documentation on IPC
    data for the Central African Republic)
  download_url: https://data.humdata.org/dataset/5123033a-2db1-496c-b381-df804ac30595/resource/eeddfe63-7c36-49d5-a0a2-f6e072f0179c/download/ipc_centralafricanrepublic.pdf
  format: null
  id: resource_eeddfe63
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IPC_CentralAfricanRepublic.pdf
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-food_security_a_datacadreharmonisechinteg_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  - CAF
  - CMR
  - TCD
  - COG
  - GAB
  - GNQ
  - STP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-08-31'
  start: '2014-01-01'
temporal_resolution: null
title: West & Central Africa Food Security Data - Cadre Harmonise (CH) and Integrated
  Food Security Phase Classification (IPC) data
version: null
vulnerability: null
---
