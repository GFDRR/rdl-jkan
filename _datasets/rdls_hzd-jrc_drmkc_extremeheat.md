---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Facility for Disaster Reduction and Recovery (GFDRR)
    url: https://www.gfdrr.org/en
  id: Entity_1
  role: resource_provider
- entity:
    affiliation: null
    email: vito@vito.be
    name: VITO NV
    url: https://www.vito.be
  id: Entity_2
  role: collaborator
catalog: World Bank Data Catalog
contact_point:
  affiliation: null
  email: mamadio@worldbank.org
  name: Mattia Amadio
  url: https://www.gfdrr.org/en
creator:
  affiliation: null
  email: null
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
dataset_id: rdls_hzd-jrc_drmkc_extremeheat
description: Probabilistic modelling of extreme heat hazard
details: "Extreme Heat hazard is classified based on an existing and widely accepted\
  \ heat stress indicator, the Wet Bulb Globe Temperature (WBGT, in \xB0C) \u2013\
  \ more specifically the daily maximum WGBT. The WBGT has an obvious relevance for\
  \ human health, but it is relevant in all kinds of projects and sectors, including\
  \ infrastructure related, as heat stress affects personnel and stakeholders, and\
  \ therefore the design of buildings and infrastructure. Heat stress studies in the\
  \ scientific literature that make use of the WBGT apply thresholds of 28\xB0C and\
  \ 32\xB0C to categorise heat stress risk. The damaging intensity thresholds are\
  \ applied following this definition of slight/low (32\xB0C) heat stress."
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: GFDRR_Extreme_Heat_Hazard
        intensity_measure: WBGT:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: '5'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: GFDRR_Extreme_Heat_Hazard
        intensity_measure: WBGT:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: '20'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: GFDRR_Extreme_Heat_Hazard
        intensity_measure: WBGT:C
        process: extreme_heat
        trigger: null
        type: extreme_temperature
      id: '100'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    frequency_distribution: null
    hazards:
    - classification: null
      id: GFDRR_Extreme_Heat_Hazard
      intensity_measure: WBGT:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: Extreme_Heat_Hazard
    occurrence_range: 1/5 to 1/100 years
    seasonality: null
license: CC0-1.0
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: Global Facility for Disaster Reduction and Recovery (GFDRR)
    risk_data_type: null
    type: model
    url: https://www.gfdrr.org/en
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Development of a hazard screening protocol for Extreme Heat
  url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0087127/VITO%20-%20Extreme%20heat%20Final_report_v2.pdf
publisher:
  affiliation: null
  email: null
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To assess extreme heat hazard across regions using the Wet Bulb Globe Temperature
  (WBGT) indicator to support human health protection, infrastructure design, and
  heat stress risk management.
referenced_by:
- author_names:
  - Koen De Ridder
  - Dirk Lauwaet
  - Hans Hooyberghs
  - Filip Lefebre
  date_published: '2017-03-17'
  doi: null
  id: Ref_1
  name: Development of a hazard screening protocol for Extreme Heat
  url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0087127/VITO%20-%20Extreme%20heat%20Final_report_v2.pdf
resources:
- access_url: https://datacatalog.worldbank.org/search/dataset/0040194/Global-extreme-heat-hazard
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Probabilistic extreme heat hazard maps (the daily maximum of Wet Bulb\
    \ Globe Temperature, in \xB0C) for the 5-year return period, for Global "
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0050009/GLB_HS_RP5.tif
  format: null
  id: Extreme_Heat_Hazard_RP5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: Extreme Heat Hazard with 5 year Return Period
- access_url: https://datacatalog.worldbank.org/search/dataset/0040194/Global-extreme-heat-hazard
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Probabilistic extreme heat hazard maps (the daily maximum of Wet Bulb\
    \ Globe Temperature, in \xB0C) for the 20-year return period, for Global "
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0050005/GLB_HS_RP20.tif
  format: null
  id: Extreme_Heat_Hazard_RP20
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: Extreme Heat Hazard with 20 year Return Period
- access_url: https://datacatalog.worldbank.org/search/dataset/0040194/Global-extreme-heat-hazard
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Probabilistic extreme heat hazard maps (the daily maximum of Wet Bulb\
    \ Globe Temperature, in \xB0C) for the 100-year return period, for Global "
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0050007/GLB_HS_RP100.tif
  format: null
  id: Extreme_Heat_Hazard_RP100
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal: null
  temporal_resolution: null
  title: Extreme Heat Hazard with 100 year Return Period
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-jrc_drmkc_extremeheat
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Global Extreme Heat Hazard
version: '3'
vulnerability: null
---
