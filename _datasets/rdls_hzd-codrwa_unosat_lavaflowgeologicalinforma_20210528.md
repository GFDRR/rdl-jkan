---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/lava-flow-and-geological-information-related-to-the-volcanic-eruption-in-dr-congo-and-rwan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/lava-flow-and-geological-information-related-to-the-volcanic-eruption-in-dr-congo-and-rwan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/lava-flow-and-geological-information-related-to-the-volcanic-eruption-in-dr-congo-and-rwan
dataset_id: rdls_hzd-codrwa_unosat_lavaflowgeologicalinforma_20210528
description: 'UNOSAT code: VO20210523COD This map illustrates the lava flow extent
  and the related geological information north of Goma airport, Nord-Kivu province,
  D.R. of the Congo as detected by satellite images acquired after the eruption of
  the Mount Nyiragongo on 22 May 2021. UNITAR-UNOSAT analysis used Sentinel-2 and
  SAOCOM-1A images acquired on 27 May 2021, at respectively 08:30 UTC and 02:21 UTC,
  to extract the lava flow extent. Within this map, three vents have been identified
  along the hillside south of Nyiragongo caldera. In addition, about 10 km of fissures
  have been mapped and are mainly in NNE-SSW and NNW-SSE directions. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/lava-flow-and-geological-information-related-to-the-volcanic-eruption-in-dr-congo-and-rwan]'
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: h_vaf:mm
      process: lava
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-2 and SAOCOM-1A satellite images
    acquired on 27 May 2021 to extract lava flow extent and identify three volcanic
    vents and approximately 10 km of fissures from the Mount Nyiragongo eruption of
    22 May 2021. The analysis involved comparative review of satellite imagery to
    delineate hazard boundaries in Nord-Kivu province, D.R. Congo.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/lava-flow-and-geological-information-related-to-the-volcanic-eruption-in-dr-congo-and-rwan
  rel: source
loss: null
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
  description: Lava flow and geological information related to the volcanic eruption
    in DR Congo and Rwanda as of 27 May 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/CD/VO20210523COD/VO20210523COD_gdb.zip
  format: Geodatabase
  id: resource_366a7f37
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20210523COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Lava flow and geological information related to the volcanic eruption
    in DR Congo and Rwanda as of 27 May 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/CD/VO20210523COD/VO20210523COD_SHP.zip
  format: null
  id: resource_346b6039
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VO20210523COD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-codrwa_unosat_lavaflowgeologicalinforma_20210528
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-05-28'
temporal_resolution: null
title: Lava flow and geological information related to the volcanic eruption in DR
  Congo and Rwanda as of 27 May 2021
version: null
vulnerability: null
---
