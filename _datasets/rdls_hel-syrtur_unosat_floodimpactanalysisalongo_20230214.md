---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-analysis-along-the-orontes-river-al-assi-syrian-turkyie-boarder-as-of-9-febru
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-analysis-along-the-orontes-river-al-assi-syrian-turkyie-boarder-as-of-9-febru
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-analysis-along-the-orontes-river-al-assi-syrian-turkyie-boarder-as-of-9-febru
dataset_id: rdls_hel-syrtur_unosat_floodimpactanalysisalongo_20230214
description: "UNOSAT code EQ20230206SYR, GDACS Id: 1357372 This map illustrates satellite-detected\
  \ water along the Orontes (Al Assi) River on the Syria-T\xFCrkyie boarder close\
  \ to the Al Tloul and Jakara towns from a Sentinel-2 imagery acquired on 9 February\
  \ 2023, and from a Worldview-2 imagery aquired on the 13 February 2023. Within the\
  \ analyzed area of 210 km2 about 18 km2 appears to be flooded. The floods may have\
  \ been likely triggered by the opening of dams and the damage induced to certain\
  \ water infrastructures along the river by the tremors. This is a preliminary analysis\
  \ and has not yet been validated in the field. Please send ground feedback to United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-analysis-along-the-orontes-river-al-assi-syrian-turkyie-boarder-as-of-9-febru]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: "Building stock in settlements (Al Tloul and Jakara towns) within\
      \ the 210 km\xB2 analysis area"
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared Sentinel-2 imagery (9 February 2023) and\
    \ Worldview-2 imagery (13 February 2023) to detect satellite-observed water extent\
    \ along the Orontes River following the 6 February 2023 earthquake. The analysis\
    \ identified approximately 18 km\xB2 of flooded area within a 210 km\xB2 study\
    \ region, with flooding potentially triggered by dam opening and earthquake-induced\
    \ damage to water infrastructure."
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
- href: https://data.humdata.org/dataset/flood-impact-analysis-along-the-orontes-river-al-assi-syrian-turkyie-boarder-as-of-9-febru
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding detected via satellite
      imagery comparison
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
  description: "Flood Impact Analysis along the Orontes River (Al Assi), Syrian-T\xFC\
    rkyie boarder, as of 9 February 2023 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3492/EQ20230206SYR_gdb.zip
  format: Geodatabase
  id: resource_caa4d3ad
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Flood Impact Analysis along the Orontes River (Al Assi), Syrian-T\xFC\
    rkyie boarder, as of 9 February 2023 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3492/EQ20230206SYR_SHP.zip
  format: null
  id: resource_0702da89
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230206SYR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-syrtur_unosat_floodimpactanalysisalongo_20230214
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - TUR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-02-14'
temporal_resolution: null
title: "Flood Impact Analysis along the Orontes River (Al Assi), Syrian-T\xFCrkyie\
  \ boarder, as of 9 February 2023"
version: null
vulnerability: null
---
