---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-and-evolution-in-maroantsetra-area-analanjirofo-region-madagascar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-extent-and-evolution-in-maroantsetra-area-analanjirofo-region-madagascar
dataset_id: rdls_hl-mdg_unosat_detectedwatersextentevolu_20170313
description: 'This map illustrates satellite-detected flood waters extent and evolution
  between 08 and 10 March 2017 over Maroantsetra area, Analanjirofo region in Madagascar
  as detected by TerraSAR-X radar images acquired on 10 and 08 March 2017. Between
  08 and 10 March 2017 and within this map extent, waters receded from about 4,270
  ha of lands. Many areas within this zone remain affected and ~6,230 ha of lands
  were still flooded on the 10 March 2017 whereas ~10,500 ha of lands were flooded
  the 08 March 2017. It corresponds to about 40% decrease. It is likely that flood
  waters have been systematically underestimated along highly vegetated areas along
  main river banks and within built-up urban areas because of the special characteristics
  of the satellite data used. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-extent-and-evolution-in-maroantsetra-area-analanjirofo-region-madagascar]'
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
  description: UNOSAT analysts processed TerraSAR-X synthetic aperture radar (SAR)
    imagery from 8 and 10 March 2017 to detect and map flood water extent in the Maroantsetra
    area. Multi-temporal image comparison identified water bodies and quantified areal
    changes (4,270 ha recession, 6,230 ha remaining flooded on 10 March, 10,500 ha
    on 8 March), representing a 40% decrease in inundated area over the 2-day period.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-extent-and-evolution-in-maroantsetra-area-analanjirofo-region-madagascar
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct flood inundation extent and areal change in natural and agricultural
      lands from observed satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Satellite Detected Waters Extent and Evolution in Maroantsetra area,
    Analanjirofo region, Madagascar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20170118MOZ/FL20170118MOZ.gdb.zip
  format: Geodatabase
  id: resource_2517d36d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170118MOZ.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters Extent and Evolution in Maroantsetra area,
    Analanjirofo region, Madagascar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20170118MOZ/FL20170118MOZ_SHP.zip
  format: null
  id: resource_8bdf091d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170118MOZ_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mdg_unosat_detectedwatersextentevolu_20170313
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-03-13'
temporal_resolution: null
title: Satellite Detected Waters Extent and Evolution in Maroantsetra area, Analanjirofo
  region, Madagascar
version: null
vulnerability: null
---
