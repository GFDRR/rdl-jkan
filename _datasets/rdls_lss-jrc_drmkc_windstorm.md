---
attributions: []
catalog: JRC DRMKC risk hub
contact_point:
  affiliation: null
  email: jrc-risk-data-hub@ec.europa.eu
  name: Risk Data Hub
  url: https://joint-research-centre.ec.europa.eu/
creator:
  affiliation: null
  email: jrc-risk-data-hub@ec.europa.eu
  name: European Commission (EC), Joint Research Centre (JRC)
  url: https://joint-research-centre.ec.europa.eu/
dataset_id: rdls_lss-jrc_drmkc_windstorm
description: This dataset presents probabilistic windstorm risk estimates across Europe,
  derived from extratropical cyclone hazard modeling combined with building stock
  exposure and structural vulnerability assessments. Disaster risk is assessed through
  a probabilistic approach. Probabilistic hazard data provides the foundation. Exposure
  is determined by the overlap between hazards and assets, representing the presence
  of assets within a hazard's footprint. This allows the computation of Expected Annual
  Loss (EAL). The EAL values are then combined with vulnerability indicators and normalised
  to produce risk estimates across Europe. All outputs are provided via the H3 grid
  system, ensuring a consistent spatial representation. The dataset quantifies direct
  economic losses to structures and impacts to population from windstorm events driven
  by extratropical cyclones, enabling stakeholders to understand spatial patterns
  of windstorm risk and prioritize risk reduction investments.
details: 'The windstorm risk estimates are computed through a comprehensive probabilistic
  framework that integrates three core components: (1) probabilistic windstorm hazard
  modeling based on synthetic storm catalogs representing thousands of years of potential
  extratropical cyclone events across Europe, with wind speeds derived from atmospheric
  modeling and validated against historical observations; (2) exposure data incorporating
  building footprints from built environment datasets and population distribution
  from demographic data sources, with exposures mapped to the H3 hexagonal grid system
  for consistent spatial representation; and (3) vulnerability relationships (damage
  functions) that translate wind speeds into expected damage ratios for different
  building types, calibrated using historical loss data and engineering assessments.
  The Expected Annual Loss (EAL) calculations account for the full probability distribution
  of wind hazard intensities and their associated impacts, weighted by building values
  and population counts. All risk metrics are normalized to enable cross-regional
  comparisons and integrated with socioeconomic vulnerability indicators from the
  Risk Data Hub vulnerability dataset. The outputs are provided in EPSG:3857 projection
  (Web Mercator) and available as vector data in shapefile format, facilitating integration
  with other geospatial datasets and GIS platforms. This dataset complements the standalone
  hazard, exposure, and vulnerability datasets also available through the JRC Risk
  Data Hub, enabling users to either utilize the pre-computed risk estimates or conduct
  custom risk analyses using the component datasets. The methodology follows international
  best practices for probabilistic risk assessment and is consistent with the European
  Commission''s approach to multi-hazard risk assessment for disaster risk management.'
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: source_1
    license: CC-BY-4.0
    name: European windstorm hazard
    risk_data_type: null
    type: dataset
    url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas/metadata/windstorm
    used_in: hazard
  - id: source_2
    license: CC-BY-4.0
    name: Global Human Settlement Layer - Built-up surface
    risk_data_type: null
    type: dataset
    url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas/metadata/built_up
    used_in: exposure
  - id: source_3
    license: CC-BY-4.0
    name: Global Human Settlement Layer - Population
    risk_data_type: null
    type: dataset
    url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas/metadata/population
    used_in: exposure
  - id: source_4
    license: CC-BY-4.0
    name: European vulnerability index
    risk_data_type: null
    type: dataset
    url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas/metadata/vulnerability_rdh
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Expected Annual Loss (EAL) estimates for direct structural damage
      to buildings from windstorm events caused by extratropical cyclones. Loss values
      are computed by convolving probabilistic windstorm hazard intensities with building
      exposure and structural vulnerability functions (damage curves) that relate
      wind speeds to expected damage ratios. The EAL represents the average annual
      economic loss in monetary terms, aggregated across the full probability distribution
      of windstorm events. Loss estimates are normalized and provided at H3 grid resolution
      to support cross-regional risk comparisons and inform building code development,
      land-use planning, and insurance applications.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: strong_wind_loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: EUR
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposure and impact estimates from windstorm events caused
      by extratropical cyclones. This metric quantifies the expected annual population
      affected by windstorms, computed by overlaying probabilistic windstorm hazard
      footprints with residential population distributions and incorporating socioeconomic
      vulnerability indicators. Population impacts are aggregated across all probabilistic
      windstorm scenarios to produce annualized exposure estimates. These metrics
      support emergency preparedness planning, evacuation strategy development, and
      assessment of population-level risk reduction needs across European regions.
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: strong_wind_loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: count
project:
  name: Risk Data Hub
  url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/
publisher:
  affiliation: null
  email: jrc-risk-data-hub@ec.europa.eu
  name: European Commission (EC), Joint Research Centre (JRC)
  url: https://joint-research-centre.ec.europa.eu/
purpose: 'This dataset was created to support disaster risk management and climate
  adaptation planning across Europe by providing harmonized, probabilistic windstorm
  risk estimates at high spatial resolution. The primary purposes include: (1) enabling
  national and local authorities to identify areas of elevated windstorm risk for
  land-use planning and building code enforcement; (2) supporting emergency management
  agencies in preparedness planning and resource allocation; (3) informing insurance
  and reinsurance portfolio analysis for windstorm-related exposures; (4) facilitating
  climate change adaptation strategies by providing a baseline for assessing how windstorm
  risk may evolve under changing climate conditions; and (5) contributing to European-level
  risk assessments and the implementation of the Sendai Framework for Disaster Risk
  Reduction by providing comparable risk metrics across jurisdictions.'
referenced_by:
- author_names:
  - Samuel ROESLIN
  - Tiberiu-Eugen ANTOFIE
  - Christos BOUNTZOUKLIS
  - Andrea SIBILIA
  - Davide RODOMONTI
  - Sandro SALARI
  - Christina CORBANE
  date_published: '2025-10-29'
  doi: http://data.europa.eu/89h/d9e8cde8-e7e9-411e-9a9c-68dd0229b273
  id: reference_1
  name: Probabilistic Disaster Risk
  url: https://data.jrc.ec.europa.eu/dataset/d9e8cde8-e7e9-411e-9a9c-68dd0229b273
resources:
- access_url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3857
  description: Vector dataset containing probabilistic windstorm risk estimates for
    residential buildings across Europe. Includes Expected Annual Loss (EAL) values
    for structural damage to residential properties from extratropical cyclone windstorms.
    Risk metrics are computed by combining probabilistic windstorm hazard intensities
    with residential building exposure data and residential-specific structural vulnerability
    relationships. Data is provided on H3 hexagonal grid cells with normalized risk
    scores to enable cross-regional comparisons of residential windstorm risk.
  download_url: null
  format: null
  id: resource_residential_buildings_risk
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: European windstorm risk - Residential buildings
- access_url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/atlas
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3857
  description: Vector dataset containing probabilistic windstorm risk estimates for
    non-residential buildings across Europe. Includes Expected Annual Loss (EAL) values
    for structural damage to commercial, industrial, and institutional buildings from
    extratropical cyclone windstorms. Risk metrics are computed by combining probabilistic
    windstorm hazard intensities with non-residential building exposure data and non-residential-specific
    structural vulnerability relationships. Data is provided on H3 hexagonal grid
    cells with normalized risk scores to enable cross-regional comparisons of non-residential
    windstorm risk.
  download_url: null
  format: null
  id: resource_nonresidential_buildings_risk
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: European windstorm risk - Non-residential buildings
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-jrc_drmkc_windstorm
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
    id: gazetteer_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: European probabilistic windstorm risk
version: '1'
vulnerability: null
---
