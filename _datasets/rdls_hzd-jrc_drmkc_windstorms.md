---
attributions:
- entity:
    affiliation: null
    email: null
    name: ETH Zurich
    url: http://www.wcr.ethz.ch/
  id: attribution_resources_provider
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: thomas.roeoesli@usys.ethz.ch
  name: "Thomas R\xF6\xF6sli"
  url: http://www.wcr.ethz.ch/
creator:
  affiliation: null
  email: null
  name: Weather and Climate Risks Group, ETH Zurich
  url: http://www.wcr.ethz.ch/
dataset_id: rdls_hzd-jrc_drmkc_windstorms
description: Windstorm hazard event set containing maximum wind gust speed per event
  on a 4.4 km geographical grid.
details: 'This data archive is publishing a probabilistic extension of the historic
  windstorm hazard event set by Windstorm Information Service. The methodology used
  to create this data archive is documented in the publication: "Comparing an insurer''s
  perspective on building damages with modelled damages from pan-European winter windstorm
  event sets: a case study from Zurich, Switzerland" by Welker, Ch, Roosli, T and
  Bresch D N (2021).Windstorm hazard event set containing maximum wind gust speed
  per event on a 4.4 km geographical grid. The hazard event set covers Europe, but
  is divided into one file per country (ISO 3166-1 definition). Each file contains
  Latitude and Longitude coordinates describing the geographical grid. Event-ID and
  further metadata describing each event and a matrix reporting the maximum wind gust
  speed in Meters per Second [m/s] per event and grid coordinate.'
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 4
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: ETH_Windstorm_Hazard
        intensity_measure: PGWS_tcy:km/h
        process: extratropical_cyclone
        trigger: null
        type: strong_wind
      id: event_id
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: ETH_Windstorm_Hazard
        intensity_measure: PGWS_tcy:km/h
        process: extratropical_cyclone
        trigger: null
        type: strong_wind
      id: frequency
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: ETH_Windstorm_Hazard
        intensity_measure: PGWS_tcy:km/h
        process: extratropical_cyclone
        trigger: null
        type: strong_wind
      id: orig
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: ETH_Windstorm_Hazard
        intensity_measure: PGWS_tcy:km/h
        process: extratropical_cyclone
        trigger: null
        type: strong_wind
      id: intensity
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: ETH_Windstorm_Hazard
      intensity_measure: PGWS_tcy:km/h
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: Windstorm_Hazard
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: ETH Zurich
    risk_data_type: null
    type: model
    url: https://www.research-collection.ethz.ch/entities/researchdata/7ebb4773-6413-4114-b96f-fba7e7e95dfe
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Risk Data Hub
  url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/
publisher:
  affiliation: null
  email: null
  name: Federal Institute of Technology in Zurich (ETH Zurich)
  url: http://www.wcr.ethz.ch/
purpose: Assessment of probabilistic windstorm hazard across Europe with maximum wind
  gust speed data for risk and damage evaluation.
referenced_by:
- author_names:
  - "Thomas R\xF6\xF6sli"
  - David Niklaus Bresch
  date_published: '2020-03-25'
  doi: https://doi.org/10.3929/ethz-b-000406567
  id: Ref_1
  name: Probabilistic Windstorm Hazard Event Set for Europe
  url: https://www.research-collection.ethz.ch/entities/researchdata/7ebb4773-6413-4114-b96f-fba7e7e95dfe
resources:
- access_url: https://www.research-collection.ethz.ch/entities/researchdata/7ebb4773-6413-4114-b96f-fba7e7e95dfe
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "HDF5 container with European windstorm hazard events on a ~4.4 km\
    \ grid for country XXX (ISO3). Includes datasets: (1) event_id \u2013 unique event\
    \ identifier; (2) frequency \u2013 yearly frequency per event; (3) orig \u2013\
    \ boolean (True = historic WISC event; False = probabilistically perturbed); (4)\
    \ intensity \u2013 matrix of maximum wind gust speed per event (axis 0) and grid\
    \ cell (axis 1), units m/s. Grid coordinates provided in centroids/lat and centroids/lon\
    \ groups. Source: WISC historic footprints extended probabilistically; see README\
    \ for methods and references."
  download_url: https://www.research-collection.ethz.ch/entities/researchdata/7ebb4773-6413-4114-b96f-fba7e7e95dfe
  format: null
  id: WISC_prob_XXX
  media_type: application/x-hdf5
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 4400
  temporal: null
  temporal_resolution: null
  title: "Probabilistic Windstorm Hazard Event Set \u2013 XXX"
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-jrc_drmkc_windstorms
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
title: Probabilistic Windstorm Hazard Event Set for Europe
version: '1'
vulnerability: null
---
