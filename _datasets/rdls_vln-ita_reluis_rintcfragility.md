---
attributions:
- entity:
    affiliation: null
    email: null
    name: Italian Department of Civil Protection (DPC)
    url: https://www.protezionecivile.gov.it
  id: attribution_funder
  role: funder
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Eugenio Chioccarelli (Univ. Mediterranea di Reggio Calabria), Iunio Iervolino
    (Univ. di Napoli Federico II)
  url: https://www.reluis.it/en/rintc-dff/
creator:
  affiliation: null
  email: null
  name: ReLUIS Working Group WP3 (2014-2022)
  url: https://www.reluis.it/en/rintc-dff/
dataset_id: rdls_vln-ita_reluis_rintcfragility
description: 'Lognormal seismic fragility functions for Italian buildings and bridges,
  developed under the RINTC project (Implicit Seismic Risk of Code-Conforming Structures,
  2014-2022). The database contains 647 fragility function entries covering five construction
  material types (unreinforced masonry, reinforced concrete, base-isolated RC, precast
  concrete, steel) and bridges. Functions are provided for both code-conforming structures
  (designed per NTC2008/NTC2018) and existing/retrofitted structures (designed per
  previous Italian codes from pre-1920 to 1990s). Each function is parameterised as
  a lognormal distribution (median eta and dispersion beta) for two performance levels:
  Usability Preventing Damage (UPD) and Global Collapse (GC) or Severe Damage (SD
  for bridges). Intensity measures are spectral accelerations Sa(T) at periods from
  0.15s to 3.0s. Over 300 structures were analysed at five representative Italian
  sites (L''Aquila, Catania, Naples, Rome, Milan) with varying seismic hazard levels
  using nonlinear dynamic analysis of 3D numerical models.'
details: 'Fragility functions were derived from nonlinear dynamic analyses of three-dimensional
  numerical models. The database is organised in 11 data sheets: code-conforming and
  evolution (existing/retrofitted) sheets for each of URM (90+50 entries), RC (84+144),
  BI (12+24), PRC (51+26), Steel (96+40), plus Bridges (30). Structural metadata includes
  construction material, design code era, design PGA, site, soil class, number of
  stories, regularity, and structural details specific to each type. Curve fitting
  methods include Maximum Likelihood (ML), Normal Probability Plot (NPP), Least Squares
  Fitting (LSF), and Direct assignment (D). URM entries include 13 masonry subtypes;
  RC entries distinguish moment-resisting frames from shear walls with optional soil-structure
  interaction; BI entries specify isolation system type (FPS, HDRB, HDRB+S); PRC entries
  specify beam-column connection and cladding type; Steel entries include plan dimensions
  and bracing configuration; Bridge entries specify structural typology, pier characteristics,
  and height.'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-nd/4.0/
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://www.reluis.it/en/rintc-dff/
  rel: source
loss:
  losses: []
project:
  name: RINTC - Implicit Seismic Risk of Code-Conforming Structures (ReLUIS-DPC 2014-2022)
  url: https://www.reluis.it/en/rintc-dff/
publisher:
  affiliation: null
  email: null
  name: ReLUIS - Rete dei Laboratori Universitari di Ingegneria Sismica
  url: https://www.reluis.it
purpose: Quantification of the implicit seismic risk (annual failure rate) of Italian
  structures designed according to current and past Italian building codes, enabling
  comparison of seismic performance across design eras and structural types.
referenced_by:
- author_names:
  - E. Chioccarelli
  - I. Iervolino
  date_published: '2024-10-01'
  doi: 10.57580/ReLUIS.WP3DB001
  id: ref_rintc_database
  name: ReLUIS-DPC RINTC Database of fragility functions, version 1.0 (beta)
  url: https://www.reluis.it/en/rintc-dff/
resources:
- access_url: https://www.reluis.it/en/rintc-dff/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Single Excel workbook containing 647 lognormal fragility function
    entries across 11 data sheets, plus About and Format documentation sheets. Data
    sheets are organised by construction material (URM, RC, BI, PRC, Steel, Bridges)
    and design category (code-conforming vs evolution/existing). Each entry provides:
    structural metadata (material, masonry type, design code/era, design PGA, site,
    soil class, stories, regularity, structural details), analysis metadata (performance
    level, curve fitting method, intensity measure), fragility parameters (eta median
    in g, beta dispersion), and publication references with hyperlinks. Intensity
    measures: Sa(0.15s) to Sa(3.0s). Performance levels: UPD (Usability Preventing
    Damage), GC (Global Collapse), SD (Severe Damage for bridges).'
  download_url: null
  format: null
  id: resource_rintc_database
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RINTC Database of Fragility Functions (Excel)
risk_data_type:
- vulnerability
schema: rdls-10
slug: rdls_vln-ita_reluis_rintcfragility
spatial:
  bbox: null
  centroid: null
  countries:
  - ITA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: RINTC Database of Fragility Functions v1.0 (beta) - Italian Seismic Building
  and Bridge Fragility
version: 1.0-beta
vulnerability:
  functions:
    damage_to_loss: []
    engineering_demand: []
    fragility:
    - analysis_details: 'Lognormal seismic fragility functions for Italian buildings
        (URM, RC, BI, PRC, Steel) covering 617 entries. Derived from nonlinear dynamic
        analysis of 3D numerical models at five Italian sites (L''Aquila, Catania,
        Naples, Rome, Milan). Two performance levels: UPD and GC. Spectral acceleration
        periods vary by structure type: Sa(0.15s) for URM, Sa(0.50s)-Sa(1.0s) for
        RC and Steel, Sa(0.50s)-Sa(3.0s) for PRC, Sa(0.50s)-Sa(2.0s) for BI. Both
        code-conforming (NTC2008/NTC2018) and existing/retrofitted structures (pre-1920
        to 1990s). Taxonomy: custom Italian building classification per ReLUIS-DPC
        conventions.'
      approach: analytical
      category: buildings
      damage_scale_name: RINTC (UPD/GC)
      damage_states_names:
      - UPD (Usability Preventing Damage)
      - GC (Global Collapse)
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_earthquake
        intensity_measure: Sa(T):g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: func_fragility_buildings
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: probability
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: Custom
    - analysis_details: 'Lognormal seismic fragility functions for 30 Italian bridge
        configurations. Structural typologies: tall viaducts, shallow viaducts, integral
        abutment overpasses, traditional overpasses, overpasses with friction pendulum
        sliders, and overpasses with high-damping rubber bearings. Spectral acceleration
        periods: Sa(0.50s) to Sa(3.0s). Two performance levels: UPD and SD. Sites:
        L''Aquila, Milan, Naples. Designed per NTC2018 and EC8-Part 2 (draft). Taxonomy:
        custom bridge classification per RINTC conventions.'
      approach: analytical
      category: infrastructure
      damage_scale_name: RINTC (UPD/SD)
      damage_states_names:
      - UPD (Usability Preventing Damage)
      - SD (Severe Damage)
      hazard_analysis_type: probabilistic
      hazard_primary:
        classification: null
        id: hazard_earthquake
        intensity_measure: Sa(T):g
        process: ground_motion
        trigger: null
        type: earthquake
      hazard_secondary: null
      id: func_fragility_bridges
      impact:
        measurement:
          quantity_kind: dimensionless_ratio
          unit: null
        metric: probability
        modelling: simulated
        type: direct
      relationship: math_parametric
      taxonomy: Custom
    socio_economic: []
    vulnerability: []
---
