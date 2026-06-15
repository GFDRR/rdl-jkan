---
attributions:
- entity:
    affiliation: null
    email: null
    name: Coastal Climate Core Services (CoCliCo) project
    url: https://coclicoservices.eu/
  id: Entity_1
  role: resource_provider
- entity:
    affiliation: null
    email: null
    name: Deltares
    url: https://deltares.nl/
  id: Entity_2
  role: processor
- entity:
    affiliation: null
    email: null
    name: "Universidad de Cantabria, Instituto de Hidr\xE1ulica Ambiental de la Universidad\
      \ de Cantabria 'IHCantabria'"
    url: https://www.ihcantabria.com
  id: Entity_3
  role: author
catalog: null
contact_point:
  affiliation: null
  email: g.lecozannet@brgm.fr
  name: "Gon\xE9ri Le Cozannet"
  url: https://brgm.fr/fr
creator:
  affiliation: null
  email: null
  name: Coastal Climate Core Services (CoCliCo) project
  url: https://coclicoservices.eu/
dataset_id: rdls_hzd-jrc_drmkc_coastalflood
description: Probabilistic modelling of coastal flood hazard
details: "Flood maps showing the maximum flood extent and depth for different extreme\
  \ scenarios (1-year, 100-year, and 1000-year return period TWL events), various\
  \ relative SLR projections (decadal time steps from 2030 to 2150 relative to the\
  \ reference period 1995\u20132014 for three SSP scenarios and one high-end scenario),\
  \ and the combination of each extreme scenario with every sea level rise scenario."
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 4
      events:
      - calculation_method: simulated
        description: 'Static water level: maximum flood extent and depth at a given
          sea level (no return period applied). Available across all defense levels,
          climate scenarios (SSP1-2.6, SSP2-4.5, SSP5-8.5, High-End), and time horizons
          (2010, 2030, 2050, 2100, 2150 for High-End) via the STAC collection.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: CoCliCo_Coastal_Flood_Hazard
          intensity_measure: fl_wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: cfhp_static
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: null
            probability:
              span: 1
              value: null
            return_period: null
      - calculation_method: simulated
        description: '1-year return period (63% probability of exceedance in 1 year):
          maximum flood extent and depth. Available across all defense levels, climate
          scenarios (baseline, SSP1-2.6, SSP2-4.5, SSP5-8.5, High-End), and time horizons
          (2010, 2030, 2050, 2100) via the STAC collection.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: CoCliCo_Coastal_Flood_Hazard
          intensity_measure: fl_wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: cfhp_1yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 1.0
            probability:
              span: 1
              value: 0.63212
            return_period: 1
      - calculation_method: simulated
        description: '100-year return period (1% annual exceedance probability): maximum
          flood extent and depth. Available across all defense levels, climate scenarios
          (baseline, SSP1-2.6, SSP2-4.5, SSP5-8.5, High-End), and time horizons (2010,
          2030, 2050, 2100) via the STAC collection.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: CoCliCo_Coastal_Flood_Hazard
          intensity_measure: fl_wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: cfhp_100yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.01
            probability:
              span: 100
              value: 0.63212
            return_period: 100
      - calculation_method: simulated
        description: '1000-year return period (0.1% annual exceedance probability):
          maximum flood extent and depth. Available across all defense levels, climate
          scenarios (baseline, SSP1-2.6, SSP2-4.5, SSP5-8.5, High-End), and time horizons
          (2010, 2030, 2050, 2100) via the STAC collection.'
        disaster_identifiers: []
        hazard:
          classification: null
          id: CoCliCo_Coastal_Flood_Hazard
          intensity_measure: fl_wd:m
          process: coastal_flood
          trigger: null
          type: flood
        id: cfhp_1000yr
        occurrence:
          deterministic: null
          empirical: null
          probabilistic:
            event_rate: 0.001
            probability:
              span: 1000
              value: 0.63212
            return_period: 1000
      frequency_distribution: null
      hazards:
      - classification: null
        id: CoCliCo_Coastal_Flood_Hazard
        intensity_measure: fl_wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: Coastal_Flood_Hazard
      occurrence_range: 1/1 to 1/1000 years
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: Coastal Climate Core Services (CoCliCo) project
    risk_data_type: null
    type: model
    url: https://coclicoservices.eu/
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Coastal Climate Core Services (CoCliCo)
  url: https://coclicoservices.eu/
publisher:
  affiliation: null
  email: null
  name: Coastal Climate Core Services (CoCliCo) project
  url: https://coclicoservices.eu/
purpose: To assess coastal flood extent and depth under various extreme event scenarios
  and sea level rise projections from 2030 to 2150 to support coastal risk management
  and adaptation planning.
referenced_by:
- author_names:
  - Camila Cotrim
  - Alexandra Toimil
  - "I\xF1igo Losada"
  - Melisa Menendez
  - Hector Lobeto
  - "Iria Su\xE1rez"
  - Sara Novo
  date_published: '2025-05-29'
  doi: https://doi.org/10.9753/icce.v38.management.202
  id: Ref_1
  name: EUROPEAN ASSESSMENT OF COASTAL FLOOD HAZARDS
  url: https://icce-ojs-tamu.tdl.org/icce/article/view/14640
resources:
- access_url: https://radiantearth.github.io/stac-browser/#/external/storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cfhp_all/collection.json?.language=en
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: 'Collection of 240 Cloud Optimized GeoTIFF flood maps at 25 m resolution
    covering European coastal areas, modelled with the RFSM-EDA hydraulic model. Maps
    span four dimensions: (1) coastal protection level - High Defended (NUTS2 policy-based
    maximum), Low Defended, Undefended (no policy protection beyond DEM); (2) return
    period - static water level (no RP), 1 year, 100 years, 1000 years; (3) climate
    scenario - no scenario (2010 baseline), SSP1-2.6, SSP2-4.5, SSP5-8.5, High-End
    (P83 of SSP5-8.5 including low-confidence processes); (4) time horizon - 2010
    (hindcast), 2030 (near-term), 2050 (mid-century), 2100 (end-of-century), 2150
    (High-End scenario only). Each raster cell contains maximum flood depth in metres.
    Access individual COG layers through the STAC catalogue or STAC Browser link.'
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cfhp_all/collection.json
  format: null
  id: cfhp_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 25
  temporal: null
  temporal_resolution: null
  title: Coastal Flood Hazard and Projections (CFHP) - STAC Collection (Cloud Optimized
    GeoTIFF)
- access_url: https://coclico.avi.deltares.nl/geoserver/gwc/service/wmts
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: OGC WMTS endpoint via the CoCliCo GeoServer for map visualization of
    the CFHP flood maps. Provides tile-based access to aggregated flood statistics
    at LAU/NUTS administrative unit level across Europe.
  download_url: null
  format: null
  id: cfhp_wmts
  media_type: application/xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal Flood Hazard and Projections (CFHP) - WMTS Visualization
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-jrc_drmkc_coastalflood
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Coclico Coastal Hazards and Flood Risk
version: '1'
vulnerability: null
---
