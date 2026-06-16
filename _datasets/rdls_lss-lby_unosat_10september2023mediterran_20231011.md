---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp
dataset_id: rdls_lss-lby_unosat_10september2023mediterran_20231011
description: 'UNOSAT code FL20230912LBY, GDACS Id: 1102204 On the night of the 10th
  of September 2023, after its journey through the Mediterranean Sea, the storm Daniel
  brought heavy rains that triggered floods in Benghazi, Almarj, Al Jabal Al Akhdar
  and Derna Governorates, in northeastern Libya. The increase of water levels in the
  region caused the collapse of two dams located upstream Derna River and the consequences
  was tremendous. The dam breach released a massive amount of water and a huge flood
  wave wiped out entire neighbourhoods in the city of Derna. Hundreds of people were
  reported missing by the Libyan Red Crescent Society. According to the Libyan National
  Meteorological Centre, the storm reached its peak with winds going up to 70-80 km/h.
  This led to the falling of electricity towers and tress causing communications interruption.
  Between 150 - 240 mm were reported and caused flash floods in several cities. Al-Bayda
  have recorded the highest daily rainfall rate: 414.1 mm in the night of the 10 to
  11 September 2023.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts conducted post-event satellite imagery analysis comparing
    pre- and post-Storm Daniel images to identify and map building damage and flood
    extent in northeastern Libya. Damage was classified and validated through visual
    interpretation of satellite data, with results delivered as vector geodatabase
    and shapefile formats containing damage site locations, confidence levels, and
    damage classifications.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/10-september-2023-mediterranean-sea-storm-daniel-in-libya-preliminary-satellite-based-comp
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding caused by Storm Daniel
      and dam collapse in Derna
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Fatalities from fluvial flooding in northeastern Libya
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
        metric: casualty_count
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
  description: 10 September 2023 Mediterranean Sea Storm Daniel in Libya, Preliminary
    Satellite-Based Comprehensive Damage Assessment Report (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3687/FL20230912LBY_gdb.zip
  format: Geodatabase
  id: resource_e988ddaa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 10 September 2023 Mediterranean Sea Storm Daniel in Libya, Preliminary
    Satellite-Based Comprehensive Damage Assessment Report (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3687/FL20230912LBY_SHP.zip
  format: null
  id: resource_0106e482
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lby_unosat_10september2023mediterran_20231011
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-11'
temporal_resolution: null
title: 10 September 2023 Mediterranean Sea Storm Daniel in Libya, Preliminary Satellite-Based
  Comprehensive Damage Assessment Report
version: null
vulnerability: null
---
