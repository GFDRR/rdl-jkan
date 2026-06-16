---
attributions:
- entity:
    affiliation: null
    email: null
    name: RED - Risk, Engineering  Development - Pavia (Italy)
    url: https://www.redrisk.com
  id: CA_SFRARR_RED
  role: principal_investigator
catalog: null
contact_point:
  affiliation: null
  email: paola.ceresa@redrisk.com
  name: Paola Ceresa
  url: null
creator:
  affiliation: null
  email: null
  name: Gabriele Coccia
  url: https://www.cimafoundation.org
dataset_id: rdls_hzd-wb_centralasiafloodhistorica
description: Fluvial flood hazard map for the historical scenario of the Hamadoni
  flood on the Panj River (Tajikistan, June-July 2005) and realistic scenarios for
  100 years return period.
details: 'Data from the EU-funded ''Strengthening Financial Resilience and Accelerating
  Risk Reduction in Central Asia'' Program (https://www.gfdrr.org/en/program/SFRARR-Central-Asia).
  Exposure data developed using high-resolution global and regional datasets and local
  official data, harmonized to produce a regionally-consistent exposure database for
  Central Asia. The exposure database includes: population, residential buildings,
  non-residential buildings (schools, healthcare facilities, industrial and commercial
  buildings), croplands, transportation system (roads, railways and bridges), airports
  and airstrips, mines, and supply infrastructure. The exposure database developed
  during this project can be used at regional scale, national scale or sub-national
  scale (e.g., at Oblast scale).'
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 1
    events:
    - calculation_method: inferred
      description: null
      disaster_identifiers:
      - description: null
        id: 2005-0370-TJK
        scheme: EMDAT
        title: null
        uri: null
      hazard:
        classification: null
        id: '1'
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: TJK_Hamadoni
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 3
    frequency_distribution: null
    hazards:
    - classification: null
      id: '1'
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: CA_SFRARR_FL_hist
    occurrence_range: null
    seasonality: null
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 3
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: '2'
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: Three_100y_events
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 1
            value: 0.01
          return_period: 100
    frequency_distribution: null
    hazards:
    - classification: null
      id: '2'
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: CA_SFRARR_FL_100y
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: SFRARR - Strengthening Financial Resilience and Accelerating Risk Reduction
    in Central Asia
  url: null
publisher:
  affiliation: null
  email: null
  name: RED - Risk, Engineering  Development - Pavia (Italy)
  url: https://www.redrisk.com/
purpose: Scenario modelling of selected floods representative of an extreme event
  in three countries (KGZ, TKM, UZB) and one historical scenario (TJK). Used for validation
  of flood modelling approach against historical observations and to communicate potential
  extreme flood impacts.
referenced_by:
- author_names: null
  date_published: '1905-07-14'
  doi: null
  id: SFRARR_FloodReport_English
  name: Task 3 Flood Hazard Assessment Report - Regionally consistent risk assessment
    for earthquakes and floods and selective landslide scenario analysis for strengthening
    financial resilience and accelerating risk reduction in Central Asia(SFRARR Central
    Asia disaster risk assessment)
  url: https://datacatalogfiles.worldbank.org/ddh-published/0064084/DR0090774/Task3_FloodHazard_Report_r5_EN.pdf?versionId=2023-07-21T17:34:14.1038579Z
- author_names: null
  date_published: '1905-07-14'
  doi: null
  id: SFRARR_FloodReport_Russian
  name: Task 3 Flood Hazard Assessment Report - Regionally consistent risk assessment
    for earthquakes and floods and selective landslide scenario analysis for strengthening
    financial resilience and accelerating risk reduction in Central Asia(SFRARR Central
    Asia disaster risk assessment)
  url: https://datacatalogfiles.worldbank.org/ddh-published/0064084/DR0090783/Task3_FloodHazard_Report_r5_RU.pdf?versionId=2023-07-21T17:34:24.6069148Z
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Fluvial flood hazard map ( i.e., a map where each pixel represents
    the maximum water depth ) for the historical scenario of the Hamadoni flood on
    the Panj River (Hamadoni, Tajikistan, June-July 2005). The simulated hydrograph
    was estimated from data reported by JICA (https://openjicareport.jica.go.jp/pdf/11870748_01.pdf).
    We assumed a bankfull discharge of 3-year return time.
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0064165/DR0090876/maxwd_Hamadoni.tif?versionId=2023-07-21T17:20:16.5760431Z
  format: geotiff
  id: CA_SFRARR_Hamadoni
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2005_Flood_Panj_Hamadoni_TJK
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Fluvial flood hazard maps for a realistic scenarios estiamted at 1-in-100
    years return period for Turkmenabat, Turkmenistan. Realistic scenarios were identified
    to assess potential floods that have not happened in the past but may affect the
    region in the future. For this reason, we asked our local experts in the consortium
    to provide indications on the areas where our realistic scenarios should be implemented.
    Specifically, we applied the following criteria: (1) flood prone area; (2) populated
    and built area exposed to flood risk; (3) floods happened in the area in the past.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0064166/DR0090880/Scenario_3_Turkmenabat_TKM_100y.tif?versionId=2023-07-21T17:20:00.4661664Z
  format: geotiff
  id: CA_SFRARR_FL_100y
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 100y_Fl_scenario_Turkmenabat_TKM
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-wb_centralasiafloodhistorica
spatial:
  bbox:
  - 69.415864227
  - 37.168360403
  - 70.215864563
  - 37.968361001
  centroid: null
  countries:
  - KAZ
  - KGZ
  - TKM
  - TJK
  - UZB
  gazetteer_entries: []
  scale: sub-national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Central Asia flood historical scenarios
version: '2022'
vulnerability: null
---
