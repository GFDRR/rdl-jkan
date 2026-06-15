---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2A satellite
    url: https://data.humdata.org/dataset/northern-syria-burned-land-analysis-dataset-may-june-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/northern-syria-burned-land-analysis-dataset-may-june-2019
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/northern-syria-burned-land-analysis-dataset-may-june-2019
dataset_id: rdls_hzd-syr_reach_northernburnedlandanalysi_20190630
description: 'Using 10m resolution multispectral imagery from the Sentinel-2A satellite,
  a relativized burn ratio (RBR) was calculated and used for burned land classification
  to assess and quantify areas which have been burned between 4 May and 30 June 2019
  in the governorates of Al-Hasakeh, Deir-ez-Zor, Ar-Raqqa, Aleppo, Idleb and Northern
  Hama. The before and after images are composites ranging from 6 April to 3 May 2019
  and 27 to 30 June 2019.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/northern-syria-burned-land-analysis-dataset-may-june-2019]'
details: The RBR analysis does not distinguish whether burned land was before or after
  the harvest of the specific cropland.
exposure: []
hazard:
  event_sets_by_hazard_type:
    wildfire:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Sentinel-2A multispectral imagery from before (6 April - 3 May 2019)
    and after (27-30 June 2019) periods was processed to calculate relativized burn
    ratio (RBR) at 10m resolution. RBR classification was applied to delineate burned
    land polygons across six Syrian governorates, quantifying burned area extent during
    the May-June 2019 period.
  sources:
  - id: source_1
    license: null
    name: Sentinel-2A satellite
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/northern-syria-burned-land-analysis-dataset-may-june-2019
  rel: source
loss:
  losses: []
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
  description: Northern Syria Burned Land Analysis Dataset - May June 2019 (Shapefile)
  download_url: https://data.humdata.org/dataset/771b1f4a-d42d-40d8-874b-b0c910ecc4fe/resource/cb81ef5c-dbf8-4e0d-9923-7925b6906d2a/download/northsyria_burnedland_mayjune2019.zip
  format: null
  id: resource_cb81ef5c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NorthSyria_BurnedLand_MayJune2019.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-syr_reach_northernburnedlandanalysi_20190630
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-06-30'
temporal_resolution: null
title: Northern Syria Burned Land Analysis Dataset - May June 2019
version: null
vulnerability: null
---
