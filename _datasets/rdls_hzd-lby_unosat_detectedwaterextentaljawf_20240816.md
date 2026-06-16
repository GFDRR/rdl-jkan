---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-al-jawf-town-alkufra-governorate-east-province-libya-as-of-14-august-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-al-jawf-town-alkufra-governorate-east-province-libya-as-of-14-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-al-jawf-town-alkufra-governorate-east-province-libya-as-of-14-august-2024
dataset_id: rdls_hzd-lby_unosat_detectedwaterextentaljawf_20240816
description: "UNOSAT code: FL20240812LBY This map illustrates satellite-detected water\
  \ extent in Al-jawf Town, Alkufra Governorate, East Province, Libya as observed\
  \ from a Sentinel-2 satellite image acquired on 14 August 2024 at 11:13 UTC. Within\
  \ the analysed area of about 120km\xB2, a total of about 2 km\xB2 of lands appear\
  \ to be affected by flood water. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-al-jawf-town-alkufra-governorate-east-province-libya-as-of-14-august-2024]"
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-2 satellite image acquired on 14 August 2024 was analyzed\
    \ by UNOSAT through visual interpretation and multi-temporal comparison to detect\
    \ changes in water extent. The resulting water extent polygon was digitized and\
    \ quantified to identify approximately 2 km\xB2 of flood-affected land within\
    \ a 120 km\xB2 study area in Al-jawf Town, Libya."
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
- href: https://data.humdata.org/dataset/water-extent-in-al-jawf-town-alkufra-governorate-east-province-libya-as-of-14-august-2024
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
  description: Satellite detected water extent in Al-jawf Town, Alkufra Governorate,
    East Province, Libya as of 14 August 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3914/FL20240812LBY_gdb.zip
  format: Geodatabase
  id: resource_7590ba91
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Al-jawf Town, Alkufra Governorate,
    East Province, Libya as of 14 August 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3914/FL20240812LBY_SHP.zip
  format: null
  id: resource_09a00835
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240812LBY_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lby_unosat_detectedwaterextentaljawf_20240816
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
  start: '2024-08-16'
temporal_resolution: null
title: Satellite detected water extent in Al-jawf Town, Alkufra Governorate, East
  Province, Libya as of 14 August 2024
version: null
vulnerability: null
---
